
from django.urls import path
from .import views


urlpatterns = [
    path('', views.items, name='items'),
    path('item', views.items, name='item'),
    path('item/<id>', views.item, name='item'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('add_to_wish/<id>', views.add_to_wish, name='add_to_wish'),
    path('cart', views.cart, name='cart'),
    
    path('detail', views.detail, name='detail'),
]