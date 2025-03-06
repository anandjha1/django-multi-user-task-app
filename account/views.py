from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "login successfully")

            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, "username or password not correct.")
            

    return render(request, "login.html")

def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            try:
                User.objects.get(username=username)
                messages.error(request, "username already taken.")
                return render(request, "signup.html")
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = full_name
                user.save()
                login(request, user)
                return redirect('/')
        else:
            messages.error(request, "password does not matched")

    return render(request, "signup.html")

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "logout successfully.")
    
    return render(request, 'logout.html')