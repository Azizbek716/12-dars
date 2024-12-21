from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def home(request):
    return render(request, 'index.html')


def product_list(request):
    products = Product.objects.all()
    # products.delete()
    ctx = {'products': products}
    return render(request, 'products/product-list.html', ctx)


def product_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        image = request.FILES.get('image')
        # print(price, title, category, short_content, long_content, image)
        if title and price and category and short_content and long_content and image:
            Product.objects.create(
                title=title,
                price=price,
                category=category,
                short_content=short_content,
                long_content=long_content,
                image=image
            )
            return redirect('products:list')
    return render(request, 'products/product-create.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product': product}
    return render(request, 'products/product-detail.html', ctx)
