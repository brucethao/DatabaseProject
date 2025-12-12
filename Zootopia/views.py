from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
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
        #image map for animals
        image_map = {
            'Big Back': 'Bigback.png',
            'King Julien': 'kingjulien.png',
            'Leila': 'leila.jpeg',
            'Madison': 'Madison-1.jpg.optimal.jpg',
            'Max': 'max.jpg',
            'Mort': 'mort.png',
            'Rich': 'please work.jpg',
            'Red': 'red.jpg',
            'Rick': 'rick.jpeg',
            'Tigress': 'tigress.jpg',
            'Smoke': 'smoke.jpg', #just wanted to put my cat in here since I didn't get time to make a page for him :((
        }

        image_file = image_map.get(name, None)

        image_path = f"images/{image_file}"

        context = {
            'animal': selected_animal,
            'region': region,
            'image_path': image_path,
        }

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
            'animalmedicationlog_set'
        )
        # no direct relationship to animals, but we need it for selecting the options for a new medical record
        medications = Medication.objects.all()

        context = {
            'animals': animals,
            'medications': medications
        }
        return render(request, 'zookeeperDash.html', context)

    def post(self, request, name):
        if not request.user.is_zookeeper:
            return redirect('home')

        current_zookeeper = get_object_or_404(Zookeeper, user=request.user)
        name = name

        action = request.POST.get('action')

        if action == 'add_feed':
            AnimalFeedingLog.objects.create(
                animal_id=request.POST.get('animal_id'),
                food_name_id=request.POST.get('food_id'),
                amount=request.POST.get('amount'),
                zookeeper=current_zookeeper,
                last_fed=timezone.now()
            )
            messages.success(request, "Feeding added successfully!")

        elif action == 'edit_feed':
            log_id = request.POST.get('feed_log_id')
            log = get_object_or_404(AnimalFeedingLog, id=log_id)
            log.food_name_id = request.POST.get('food_id')
            log.amount = request.POST.get('amount')
            log.save()
            messages.success(request, "Feeding updated!")

        elif action == 'delete_feed':
            log_id = request.POST.get('feed_log_id')
            AnimalFeedingLog.objects.filter(id=log_id).delete()
            messages.success(request, "Feeding record deleted.")

            # --- MEDICATION LOGIC ---
        elif action == 'add_med':
            AnimalMedicationLog.objects.create(
                animal_id=request.POST.get('animal_id'),
                medication_id=request.POST.get('medication_id'),
                medication_amount=request.POST.get('amount'),
                date=timezone.now()
            )
            messages.success(request, "Medical record added!")

        elif action == 'edit_med':
            log_id = request.POST.get('med_log_id')
            log = get_object_or_404(AnimalMedicationLog, id=log_id)
            log.medication_id = request.POST.get('medication_id')
            log.medication_amount = request.POST.get('amount')
            log.save()
            messages.success(request, "Medical record updated!")

        elif action == 'delete_med':
            log_id = request.POST.get('med_log_id')
            AnimalMedicationLog.objects.filter(id=log_id).delete()
            messages.success(request, "Medical record deleted.")

        return redirect(request.path)


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

class Reset(View):
    def get(self, request):
        return render(request, 'reset.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not email or not password1 or not password2:
            messages.error(request, 'Please fill all fields')
            return redirect('reset')
        elif User.objects.filter(username=username, email=email).exists():
            if password1 == password2:
                myUser = User.objects.get(username=username, email=email)
                myUser.set_password(password1)
                myUser.save()
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('reset')
        else:
            messages.error(request, 'Username does not exist\n Please try again.')
            return redirect('reset')