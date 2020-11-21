from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import SignUpForm, SignInForm

# Create your views here.

def signin(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return redirect('index')
     
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request, 'account/signin.html', {'form':form})
     
    else:
        form = AuthenticationForm()
    
    return render(request, 'account/signin.html', {'form':form})

def signup(request):
 
    if request.user.is_authenticated:
        return redirect('index')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('index')
         
        else:
            return render(request,'account/signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'account/signup.html',{'form':form})

def connexion(request):
    context={
        'connected': False
    }

    return render(request, 'account/connexion.html', context)

def my_account(request):
    context={}
    return render(request, 'account/my_account.html', context)


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')