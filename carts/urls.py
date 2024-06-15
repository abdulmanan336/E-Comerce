
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('item/<id>', views.del_cart_item, name='del_cart_item'),
    path('saves/<id>', views.del_save_item, name='del_save_item'),
    path('checkout_page', views.checkout_page, name='checkout_page'),
    path('checkout', views.checkout, name='checkout'),
    path('wish', views.wish, name='wish'),
]
