from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product

from catalog import views as c
from .models import Favorite

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

def my_account(request):
    context={}
    return render(request, 'account/my_account.html', context)


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')

def save(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            product_id = request.GET['product']
            product = get_object_or_404(Product, pk=product_id)
            user = get_object_or_404(User, pk=request.user.id)
            new_favorite = Favorite.objects.create(
                user = user,
                product = product
            )
            data = {
                'Status': 'OK'
            }
            return JsonResponse(data)

    data = {
        'Status': 'Failure'
    }
    return JsonResponse(data)
        