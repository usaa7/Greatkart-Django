from django.shortcuts import render
from store.models import Product
from category.models import Category

def home(request):
    allcategory = Category.objects.all()
    allproducts = Product.objects.all().filter(is_available = True)
    data = {
        'allproducts': allproducts,
        'allcategories': allcategory,
    }
    return render(request, 'home.html', data)


