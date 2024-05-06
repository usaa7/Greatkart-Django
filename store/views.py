from django.shortcuts import render, get_object_or_404
from store.models import Product
from . models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    categories = None
    allproducts = None
    allcategory = Category.objects.all()

    if category_slug != None:
        categories = get_object_or_404(Category, slug= category_slug)
        allproducts = Product.objects.filter(category = categories, is_available = True)
        product_count = allproducts.count()
    else:
        allproducts = Product.objects.all().filter(is_available = True)
        product_count = allproducts.count()

    data = {
        'allcategories': allcategory,
        'allproducts': allproducts,
        'product_count': product_count
    }
    return render(request, 'store/store.html', data)
 

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e: 
        raise e 

    data = {
        'product': single_product,
    } 

    return render(request, 'store/product-detail.html', data)