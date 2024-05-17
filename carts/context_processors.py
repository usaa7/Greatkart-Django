from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id = _cart_id(request))
            cartitems = CartItem.objects.all().filter(cart = cart[:1])
            for cartitem in cartitems:
                count += cartitem.quantity
        except Cart.DoesNotExist:
            count = 0
    
    return dict(cart_count = count)

            


