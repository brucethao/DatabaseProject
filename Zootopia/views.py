from django.shortcuts import render, redirect
from django.views import View

from Zootopia.models import Animals


# Create your views here.
class HomePage(View):
    def get(self, request):
        animals = Animals.objects.all()
        return render(request, 'homepage.html')
    def post(self, request):
        login = request.POST.get('login')
        register = request.POST.get('register')
        if login:
            return redirect('login')
        elif register:
            return redirect('register')
        return render(request, 'homepage.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        pass

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        pass