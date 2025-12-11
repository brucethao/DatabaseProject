from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from Zootopia.models import Animal, User, AnimalMedicationLog, AnimalFeedingLog, Medication, Zookeeper, Food


# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'homepage.html')

class AnimalPage(View):
    def get(self, request):
        return render(request, 'animal.html')

class Region(View):
    def get(self, request, region):
        animals = Animal.objects.filter(animal_habitat__continent = region)
        animals = animals.select_related('animal_habitat')

        context = {"animals": animals, "region": region}
        return render(request, 'regions.html', context)

class AnimalPageDetails(View):
    def get(self, request, region, name):
        selected_animal = get_object_or_404(
            Animal,
            name=name,
            animal_habitat__continent=region
        )

        # 2. CONTEXT
        context = {
            'animal': selected_animal,
            'region': region,
        }

        # 3. RENDER
        return render(request, 'animal_page.html', context)


"""
ZooKeeper page requires an authenticated user with is_zookeeper permission
- if not logged in -> redirect to login page
- if not zookeeper -> redirect to animals page
yall can change the logic if you want!!!
"""
class Dashboard(View):
    def get(self, request, name):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        name = request.user.first_name
        context = {"name": name}
        return render(request, 'dashboard.html', context)


from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


class Profile(View):
    def get(self, request, name):
        # 1. Your Manual Auth Check
        user = request.user
        if not user.is_authenticated:
            return redirect('login')

        return render(request, 'profile.html')

    def post(self, request, name):
        # 1. Your Manual Auth Check
        user = request.user
        if not user.is_authenticated:
            return redirect('login')

        # 2. Update Basic Info
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        old_pass = request.POST.get('old_password')
        new_pass = request.POST.get('new_password')

        if old_pass and new_pass:
            if user.check_password(old_pass):
                user.set_password(new_pass)
                user.save()
                # Keep them logged in after password change
                update_session_auth_hash(request, user)
                messages.success(request, 'Password and Profile updated!')
            else:
                messages.error(request, 'Old password was incorrect.')
                return render(request, 'profile.html')

        user.save()
        messages.success(request, 'Profile updated successfully!')

        # Redirect back to the Profile View
        return redirect('profile', name=user.first_name)

class ZooKeeperDashboard(View):
    def get(self, request, name):
        if not request.user.is_zookeeper:
            messages.error(request, "Only zookeepers have access to the Zookeepers page.")
            return redirect('animals')

        """
        - we are grouping by animal 
        - so we need the reverse relationship for each related table -> use _set
        - there can be MANY records for each animal -> use prefetch_related for many-relationship
        """

        animals = Animal.objects.all().prefetch_related(
            'diet_set',
            'animalfeedinglog_set',
            'animalfeedinglog_set',
            'animalmedicationlog_set'
        )
        # no direct relationship to animals, but we need it for selecting the options for a new medical record
        medications = Medication.objects.all()

        context = {
            'animals': animals,
            'medications': medications
        }
        return render(request, 'zookeeperDash.html', context)

    def post(self, request):
        pass

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('home')
        else:
            messages.error(request, 'Wrong username or password')
            return render(request, 'login.html')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class VisitUs(View):
    def get(self, request):
        return render(request, 'visitus.html')
    def post(self, request):
        pass

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists. Please login or register a different user.')
            return redirect('register')
        elif password1 != password2:
            messages.info(request, 'Passwords do not match. Please try again.')
            return redirect('register')
        else:
                User.objects.create_user(
                username=username,
                password=password2,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

        return redirect('login')