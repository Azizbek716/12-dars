from django.shortcuts import render, redirect, get_object_or_404
from .models import Products


def home(request):
    articles = Products.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)


def create_products(request):
    if request.method == 'POST':
        product_lis = request.POST.get('product_lis')
        product_detail = request.POST.get('product_detail')
        product_create = request.POST.get('product_create')
        about_page = request.POST.get('long_content')
        if product_lis and product_detail and product_create and about_page:
            Products.objects.create(
                product_lis=product_lis,
                product_detail=product_detail,
                product_create=product_create,
                about_page=about_page,
            )
            return redirect('home')
    return render(request, 'products/add-post.html')


def products_by_category(request, category, about_page=None):
    articles = Products.objects.filter(about_page)
    ctx = {'articles': articles,
           'category': category}
    return render(request, 'products/articles-by-category.html', ctx)


def products_detail(request, pk):
    products = get_object_or_404(Products, pk=pk)
    ctx = {'articles': products}
    return render(request, 'products/detail.html', ctx)


