# In create_orders.py

from django.core.management.base import BaseCommand
from apps.services.retail.orders.models import Order
from apps.services.retail.customers.models import  Customer
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Creates 10 sample orders'

    def handle(self, *args, **kwargs):
        # Loop to create 10 orders
        customer = Customer.objects.all() 
        
        for i in range(1, 11):
            order = Order.objects.create(
                customer=random.choice(customer),
                billing_address=f'Billing Address {i}',
                billing_city=f'Billing City {i}',
                billing_zipcode=f'Billing Zipcode {i}',
                payment_method=f'Payment Method {i}',
                shipping_method=f'Shipping Method {i}',
                coupon_code=f'Coupon Code {i}',
                transaction_id=f'Transaction ID {i}',
                is_paid=True if i % 2 == 0 else False,  # Example condition for is_paid
                order_date=timezone.now(),
                sub_total=i * 100,  # Example value, adjust as needed
                sub_shipping=i * 10,  # Example value, adjust as needed
                shipping_cost=i * 5,  # Example value, adjust as needed
                # order_processing=True if i % 2 == 0 else False,  # Example condition for order_processing
                # order_placed=True if i % 3 == 0 else False,  # Example condition for order_placed
                # order_shipping=True if i % 4 == 0 else False,  # Example condition for order_shipping
                # order_delivered=True if i % 5 == 0 else False,  # Example condition for order_delivered
                # order_rejected=True if i % 6 == 0 else False,  # Example condition for order_rejected
                # order_poked=True if i % 7 == 0 else False,  # Example condition for order_poked
            )
            self.stdout.write(self.style.SUCCESS(f'Order {i} created successfully with ID: {order.id}'))
