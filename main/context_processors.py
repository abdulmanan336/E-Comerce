

def main(request):
    cart = request.session.get('cart')
    saves = request.session.get('saves')
    cart_count = 0
    wish_count = 0
    if cart is not None:
        cart_count = len(cart)
    
    if saves is not None:
        wish_count = len(saves)
    
    ctx = {
        'cart_count': cart_count,
        'wish_count': wish_count,
    }
     
    return ctx
     
