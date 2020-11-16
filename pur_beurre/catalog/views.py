from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError

from .models import Product


def index(request):
    context ={}
    return render(request, 'catalog/index.html', context)

def search(request):
    query = request.GET.get('query')
    if not query :
        products = Product.objects.all()
        message = "Aucun produit n'est demandé"
    else:
        products = Product.objects.filter(name__icontains=query)

        if not products.exists():
            products = Product.objects.filter(code__icontains=query)
       
    title = "Résultats pour la recherche %s"%query
    context ={
        'products': products,
        'title': title
    }
    return render(request, 'catalog/search.html', context)