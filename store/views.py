from django.shortcuts import render, get_object_or_404
from category.models import Category
from store.models import Product


# Create your views here.
def store(request, category_slug=None):
    get_category_id = None

    if category_slug is not None:
        get_category_id = get_object_or_404(Category, slug=category_slug)  # due to __int__() in module
        products = Product.objects.all().filter(category_id=get_category_id, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }

    return render(request, 'store/store.html', context)


def product_details(request, category_slug, product_slug):
    get_product_id = get_object_or_404(Product, slug=product_slug)  # due to __int__() in module
    single_product = Product.objects.get(id=get_product_id)

    # try:
    #     single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    # except Exception as e:
    #     raise e

    context = {
        'single_product': single_product
    }
    return render(request, 'store/product/productdetails.html', context)
