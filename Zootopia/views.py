from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from Zootopia.models import Animal, User, AnimalMedicationLog, AnimalFeedingLog, Medication, Zookeeper, Food


# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'homepage.html')

class AnimalPage(View):
    def get(self, request):
        return render(request, 'animal.html')

"""
ZooKeeper page requires an authenticated user with is_zookeeper permission
- if not logged in -> redirect to login page
- if not zookeeper -> redirect to animals page
yall can change the logic if you want!!!
"""
class ZooKeeper(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    def get(self, request):
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
        return render(request, 'zookeeper.html', context)

    def post(self, request):
        # TO-DO:
        #   - implement edit function
        #   - messages...
        #   - If time permits -> add/delete/edit for Location, Animal, Food, Medication, and Diet
        # action - current working functionality: add & delete on medication records & feeding records
        # for deletion: we have direct access the two log ids -> don't have to use composite key search for unique log
        action = request.POST.get('action')
        animal_id = request.POST.get('animal_id')
        zookeeper = Zookeeper.objects.get(user=request.user) # only zookeepers can access this page -> just directly get the user

        # add medical record
        if action == 'add_med':
            medication_id = request.POST.get('medication_id')
            # number validation & min-max validation implemented inside the forms input
            amount = request.POST.get('amount')
            # date field is auto-generated & already configurated in settings to match our timezone
            AnimalMedicationLog.objects.create(
                animal_id=animal_id,
                medication_id=medication_id,
                medication_amount=amount
            )

        # delete medical record
        elif action == 'delete_med':
            med_log_id = request.POST.get('med_log_id')
            med_log = AnimalMedicationLog.objects.get(id=med_log_id).delete()

        # edit medical record
        elif action == 'edit_med':
            med_log_id = request.POST.get('med_log_id')
            medication_id = request.POST.get('medication_id')
            amount = request.POST.get('amount')
            med_log = AnimalMedicationLog.objects.get(id=med_log_id)

            # directly assign the fkey stored as medication_id in database, NOT medication (in the models)
            # otherwise you would need to grab the actual medication object and assign med_log.medication = medication
            med_log.medication_id=medication_id
            med_log.medication_amount=amount
            med_log.save()

        # add feeding record
        elif action == 'add_feed':
            food_id = request.POST.get('food_id')
            amount = request.POST.get('amount')

            AnimalFeedingLog.objects.create(
                animal_id=animal_id,
                food_name_id=food_id,
                amount=amount,
                zookeeper=zookeeper
            )

        # delete feeding record
        elif action == 'delete_feed':
            feed_log_id = request.POST.get('feed_log_id')
            feed_log = AnimalFeedingLog.objects.get(id=feed_log_id).delete()

        # edit feeding record
        elif action == 'edit_feed':
            feed_log_id = request.POST.get('feed_log_id')
            food_id = request.POST.get('food_id')
            amount = request.POST.get('amount')
            food_log = AnimalFeedingLog.objects.get(id=feed_log_id)

            # directly assign the fkey stored as food_name_id in database, NOT food_name (in the models)
            food_log.food_name_id=food_id
            food_log.amount=amount
            food_log.save()

        return redirect('zookeeper')

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
            user = User.objects.create_user(
                username=username,
                password=password2,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

        return redirect('login')