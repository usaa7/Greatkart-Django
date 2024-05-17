from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

# Create your views here.
def store(request, category_slug=None):
    categories = None
    allproducts = None
    allcategory = Category.objects.all()

    if category_slug != None:
        categories = get_object_or_404(Category, slug= category_slug)
        allproducts = Product.objects.filter(category = categories, is_available = True).order_by('id')
        paginator = Paginator(allproducts, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = allproducts.count()
    else:
        allproducts = Product.objects.all().filter(is_available = True).order_by('id')
        paginator = Paginator(allproducts, 6) 
        page = request.GET.get('page') 
        paged_products = paginator.get_page(page)
        product_count = allproducts.count()
    data = {
        'allcategories': allcategory,
        'allproducts': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', data)
 

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists() 
    except Exception as e: 
        raise e 

    data = {
        'product': single_product,
        'product_in_cart': in_cart,
    } 

    return render(request, 'store/product-detail.html', data)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('id').filter(product_name__icontains=keyword)
            product_count = products.count()
    
    data = {
        'allproducts': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', data)