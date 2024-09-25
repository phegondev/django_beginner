from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:list')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')
        else:
            messages.error(request, "Invalid username or password")
            
    return render(request, 'login.html')
        

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:list')