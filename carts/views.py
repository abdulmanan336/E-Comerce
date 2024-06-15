import uuid
from django.shortcuts import redirect, render
from items import models as imodels
from orders import models as omodels
from django.urls import reverse
from decimal import Decimal
# Create your views here.


def cart(request):
    cart = request.session.get('cart')
    items = []
    sub_total = 0
    sub_shipping = 0
    total = 0
    if cart is not None:
        items = imodels.Item.objects.filter(id__in=cart.keys())
        for item in items:
            item.qty = cart[str(item.id)]
            item.total = Decimal(item.qty) * item.get_discounted_price
            item.qty = cart[str(item.id)]
            sub_total += item.total
            sub_shipping += int(item.qty) * item.shipping_price
            total = sub_shipping + sub_total
    ctx = {
        'items': items,
        'sub_total':sub_total,
        'sub_shipping':sub_shipping,
        'total':total
    }
    return render(request,'carts/cart.html', ctx)

def del_cart_item(request, id):
    cart = request.session.get('cart')
    del cart[id]
    request.session.modified = True
    return redirect('cart')


def del_save_item(request, id):
    saves = request.session.get('saves')
    saves.remove(id)
    request.session.modified = True
    return redirect('wish')

def wish(request):
    saves = request.session.get('saves')
    items = []
    if saves is not None:
        items = imodels.Item.objects.filter(id__in=saves)

    return render(request,'carts/wish.html', { 'items': items })

from django.shortcuts import render, redirect
from decimal import Decimal

def checkout_page(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        for key, value in request.POST.items():
            if key in cart:
                cart[key] = value
                request.session.modified =  True
        
    cart = request.session.get('cart')
    items = []
    sub_total = 0
    sub_shipping = 0
    total = 0
    
    if cart is not None:
        items = imodels.Item.objects.filter(id__in=cart.keys())
        for item in items:
            item.qty = cart[str(item.id)]
            item.total = Decimal(item.qty) * item.get_discounted_price
            sub_total += item.total
            sub_shipping += int(item.qty) * item.shipping_price
        total = sub_shipping + sub_total

    ctx = {
        'items': items,
        'sub_total': sub_total,
        'sub_shipping': sub_shipping,
        'total': total
    }
    return render(request, 'main/checkout.html', ctx)


def checkout(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zipcode = request.POST.get('zipcode')

    cart = request.session.get('cart')
    # if cart.items():
    items = imodels.Item.objects.select_for_update().filter(id__in=cart.keys())

    # order_item.total = 0
    sub_total = 0
    sub_shipping = 0
    order_items = []
    order = omodels.Order(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address,city=city,state=state,zipcode=zipcode,sub_total=sub_total, sub_shipping=sub_shipping)
    for item in items:
        order_item = omodels.OrderItem(order=order, item=item)
        order_item.qty = cart[str(item.id)]
        order_item.sale_price = item.sale_price
        order_item.discount = item.discount
        order_item.shipping_price = item.shipping_price
        order_item.total =  Decimal(order_item.qty) * item.get_discounted_price
        sub_total += order_item.total
        sub_shipping += int(order_item.qty) * item.shipping_price
        if item.quantity >= int(order_item.qty):
            item.quantity -= int(order_item.qty)
            order_items.append(order_item)
        
    order.sub_total = sub_total
    order.sub_shipping = sub_shipping
    imodels.Item.objects.bulk_update(items, ['quantity'])
    order_id = uuid.uuid4()
    order.order_id = str(order_id)[:8]
    order.save()
    omodels.OrderItem.objects.bulk_create(order_items)
    del request.session['cart']
    request.session.modified = True

    return redirect(reverse('track_order')+f'?order_id={order.order_id}')
