from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('track_order', views.track_order, name='track_order'),
]