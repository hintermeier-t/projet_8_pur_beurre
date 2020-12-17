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
    else:
        products = Product.objects.filter(name__icontains=query)

        if not products.exists():
            products = Product.objects.filter(code__icontains=query)
       
    title = ("Résultats pour la recherche \"{}\":".format(query))
    context ={
        'products': products,
        'query': query,
        'title': title
    }
    return render(request, 'catalog/search.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = " ".join(
        [category.name for category in product.categories.all()]
        )
    context={
        'product_name': product.name,
        'nutriscore': product.nutriscore,
        'description': product.description,
        'brand': product.brand,
        'thumbnail': product.picture,
        'url': product.url,
        'categories': product.categories.all()
    }
    
    return render(request, 'catalog/detail.html', context)


def legal(request):
    context={
        
    }
    return render(request, 'catalog/legal.html', context)