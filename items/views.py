from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from django.db import transaction
from django.db.models import Count
# Create your views here.

def items(request):
    q = request.GET.get('q')
    req_cat = request.GET.get('category')
    offer = request.GET.get('offer')
    req_order = request.GET.get('order')
    req_brands = request.GET.getlist('brands')
    req_free_shipping = request.GET.get('free_shipping')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    try:
        min_price = int(min_price)
        max_price = int(max_price)
    except:
        min_price = None
        max_price = None
        
    items = models.Item.objects.select_related('category', 'brand').all()

    if q:
        items = models.Item.objects.filter(title__icontains=q)
        if not items:  # If no items are found
            messages.error(request, "Oooops! There is no items about your search.")
    else:
        if q == '':
            return redirect("main")
        
        
    


    if req_order is not None:
        if req_order == 'true':
            items = items.order_by('-created_at')
        if req_order == 'false':
            items = items.order_by('created_at')

    if req_cat is not None:
        items = items.filter(category__title=req_cat)
    if offer is not None:
        items = items.filter(offer__title=offer)

    if min_price is not None:
        items = items.filter(sale_price__gte=min_price)

    if max_price is not None:
        items = items.filter(sale_price__lte=max_price)

    if req_free_shipping is not None and req_free_shipping == 'true':
        items = items.filter(free_shipping=True)

    cats = items.values('category__title').annotate(items_count=Count('category__title'))
    cats = {cat['category__title']: cat['items_count'] for cat in cats}
    brands = items.values('brand__title').annotate(items_count=Count('brand__title'))
    brands = {brand['brand__title']: brand['items_count'] for brand in brands}
    offers = items.values('offer__title').annotate(items_count=Count('offer__title'))
    # cats_check = models.Item.objects.values('category__title').annotate(items_count=Count('category__title')).distinct()
    # cats_check = {cat['category__title']: cat['items_count'] for cat in cats_check}
    # print(cats_check)
    # print(brands)
    
    
    
    if req_brands is not None and len(req_brands) > 0:
        items = items.filter(brand__title__in=req_brands)
    
    if req_brands is None:
        req_brands = []
        
    paginator = Paginator(items, 9)
    page = request.GET.get('page')

    try:
        paginated_items = paginator.page(page)
    except PageNotAnInteger:
        paginated_items = paginator.page(1)
    except EmptyPage:
        paginated_items = paginator.page(paginator.num_pages)   
    
    current_page = paginated_items.number
    start_page = max(current_page - 1, 1)
    end_page = min(current_page + 1, paginator.num_pages)

    if end_page - start_page < 2:
        if start_page == 1:
            end_page = min(start_page + 2, paginator.num_pages)
        elif end_page == paginator.num_pages:
            start_page = max(end_page - 2, 1)

    pages = range(start_page, end_page + 1)
    
    ctx = {
        'items': items,
        'cats': cats,
        'brands': brands,
        'offers': offers,
        'req_brands': req_brands,
        'items': paginated_items,
        'paginator': paginator,
        'pages': pages,
        'error_messages': messages.get_messages(request)
    }
    return render(request, 'items/items.html', ctx)

def item(request, id):
    item = models.Item.objects.get(id=id)
    cart = request.session.get('cart')
    saves = request.session.get('saves')
    related_items = models.Item.objects.filter(category=item.category)
    if cart is not None:
        item.in_cart = str(item.id) in cart
        
    if saves is not None:
        item.in_wish = str(item.id) in saves
    ctx = {
        'item' : item,
        'related_items' : related_items
    }
    return render(request,'items/item.html',ctx)

def detail(request):
    return render(request,'items/detail.html')

def add_to_cart(request):
    id = request.POST.get('id')
    qty = request.POST.get('qty')
    if id is None or qty is None:
        return redirect(reverse("item", args=[id]))
    cart = request.session.get('cart')
    # request.session['cart'] = {}

    if cart is None:
        request.session['cart'] = {id : qty}
        cart = request.session.get('cart')
    else:
       cart[id] = qty
       
    # cart[id] = qty
    request.session.modified = True
    print(request.session['cart'])
    return redirect('cart')

def cart(request):
    return render(request, 'carts/cart.html')



def add_to_wish(request,id):
    
    saves = request.session.get('saves')

    if saves is None:
        request.session['saves'] = [id]
        saves = request.session.get('saves')

    if id not in saves:
       saves.append(id)
       
    request.session.modified = True
    return redirect(reverse("item", args=[id]))

def add_stock(request, id):
    stock = request.POST.get('stock')

    item = models.Item.objects.get(id=id)
    with transaction.atomic():
        if stock is not None:
            models.Stock.objects.create(item=item, quantity=stock)

    return 


