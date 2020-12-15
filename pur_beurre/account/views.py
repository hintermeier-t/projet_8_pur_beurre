from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product

from .models import Favorite
from catalog import views as c

def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
     
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request, 'account/signin.html', {'form':form, 'Error': 'Invalid'})
     
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
    if request.user.is_authenticated:
        return render(request, 'account/my_account.html')
    else:
        return redirect(request, 'index', {'Error':'Not Logged In'})


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
            new_favorite = Favorite.objects.get_or_create(
                user = user,
                product = product
            )
            return HttpResponse('209')

    return HttpResponse('500')

def mail_save(request):
    if request.user.is_authenticated:
         if request.method == 'GET':
            mail = request.GET['email']
            user = get_object_or_404(User, pk=request.user.id)
            user.email = mail
            user.save()
            return HttpResponse('209')
    return HttpResponse('500')


def my_favorites(request):
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(
            user = request.user.id
        )
        fav_list = []
        for each in favorites:
            fav_list.append(each.product)
        paginator = Paginator(fav_list, 9)
        page = request.GET.get('page')
        try:
            favorites_page = paginator.page(page)
        except PageNotAnInteger:
            favorites_page = paginator.page(1)
        except EmptyPage:
            favorites_page = paginator.page(paginator.num_pages)
        context = {
            'products': favorites_page,
            'paginate': True
            }
        return render(request, 'account/my_favorites.html', context)

def delete(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            product_id = request.GET['product']
            product = get_object_or_404(Product, pk=product_id)
            user = get_object_or_404(User, pk=request.user.id)
            favorite = get_object_or_404(Favorite, user = user.id, product=product_id)
            if favorite is not None:
                favorite.delete()
            data = {
                'Status': 'OK'
            }
            return HttpResponse('209')

    return HttpResponse('500')