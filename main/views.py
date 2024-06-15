from django.shortcuts import render
from items import models as imodels
from orders import models as omodels
from . import models as models
# Create your views here.


def main(request):
    offers = imodels.Special.objects.order_by('-created_at').all()[:2]
    main = imodels.Special.objects.order_by('-created_at').all()
    item = imodels.Item.objects.all()
    products = imodels.Item.objects.all()
    featured_items = imodels.Item.objects.filter(featured=True)[:4]
    # categories = imodels.Category.objects.filter()[:10]
    categories = imodels.Category.objects.prefetch_related('items').filter()[:10]

    for cat in categories:
        # cat.items = imodels.Item.objects.filter(category=cat).count()
        cat.items_count = cat.items.all().count()
        # cat.items.set(cat.items.all())
        

    context = {
        'item' : item,
        'main' : main,
        'offers' : offers,
        'products' : products,
        'featured_items' : featured_items,
        'category' : categories,
    }
    return render(request, 'main/main.html', context)

def checkout(request):    
    return render(request, 'main/checkout.html')

def track_order(request): 
    order_id = request.GET.get('order_id')
    order = None
    if order_id is not None and order_id != '':
        try:
            order = omodels.Order.objects.get(order_id=order_id)
        except:
            pass
    return render(request, 'main/track_order.html', {'order': order})
    # return render(request, 'main/track_order.html')

def contact(request): 
    name = request.POST.get('name')   
    email = request.POST.get('email')   
    subject = request.POST.get('subject')   
    message = request.POST.get('message')   
    
    if name is not None and name != '' and email is not None and email != '' and message is not None and message != '':
        contact = models.Contact(name=name, email=email, message=message)
        if subject is not None and subject != '':
            contact.subject = subject
        contact.save()

    return render(request, 'main/contact.html')

    
    