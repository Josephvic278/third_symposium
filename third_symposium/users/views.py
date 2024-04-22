from django.shortcuts import render, redirect
from users.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['new_password']

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error("User already exsists try another Email Address of Username!!!")
            return redirect('register')
        else:
            user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            
            if not UserData.objects.filter(user=user).exists():
                UserData.objects.create(user=user)
            login(request, user)
            return redirect('app:dashboard')
    
    if request.user.is_authenticated:
        return redirect('app:dashboard')

    return render(request, 'register.html')

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(user)
            return redirect('app:dashboard')
        else:
            messages.error("Invalid Credentials!!!")
    
    if request.user.is_authenticated:
        return redirect('app:dashbaord')
    
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:landing_page')
    return None