"""This module contains every function I DO NOT use in my final project."""

 #- From views.py
 def results(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 9)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'products': products,
        'paginate': True
        }
    return render(request, 'catalog/results.html', context)