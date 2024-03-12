from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .form import * 

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = var.email
            var.is_learner = True
            var.save()
            messages.success(request, 'Account created. Please log in to continue')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong.')
            return redirect('register')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out. Log in to continue')
    return redirect('login')


