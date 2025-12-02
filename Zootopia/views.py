from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from Zootopia.models import Animal, User

# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'homepage.html')
    def post(self, request):
        login = request.POST.get('login')
        register = request.POST.get('register')

        if login is not None:
            return redirect('login')
        if register is not None:
            return redirect('register')

        return render(request, 'homepage.html')

class ZooKeeper(View):
    def get(self, request):
        return render(request, 'zookeeper.html')
    def post(self, request):
        pass

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username, password=password)

        if user is not None:
            messages.success(request, 'Login Successful')
            if user.is_zookeeper:
                return redirect('zookeeper')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Wrong username or password')
            return render(request, 'login.html')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists. Please login or register a different user.')
            return render(request, 'register.html')
        else:
            User.objects.create(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
        return render(request, 'register.html')