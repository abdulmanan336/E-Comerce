from django.core.management.base import BaseCommand
from apps.services.retail.orders.models import OrderProduct, Order 
from apps.services.retail.products.models import  Product
from apps.services.retail.customers.models import  Customer
from decimal import Decimal
from datetime import datetime
import random

class Command(BaseCommand):
    help = 'Create 10 OrderProduct instances'

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        products = Product.objects.all()
        customer = Customer.objects.all()

        for _ in range(10):
            order_product = OrderProduct.objects.create(
                order=random.choice(orders),
                product=random.choice(products),
                qty=random.randint(1, 5),
                sale_price=random.randint(50, 200),
                discount_amount=random.randint(0, 20),
                shipping_price=random.randint(10, 50),
                shipping_date=datetime.now(),
                return_requested=random.choice([True, False]),
                return_reason='Damaged product' if random.choice([True, False]) else '',
                is_returned=random.choice([True, False]),
                refund_amount=Decimal(random.uniform(10.0, 50.0)),
                total_refunded=Decimal(random.uniform(0.0, 20.0)),
                customer=random.choice(customer),
                canceled_at=datetime.now(),
                cancellation_reason='Out of stock' if random.choice([True, False]) else '',
                estimated_delivery=datetime.now(),
                delivery_date=datetime.now(),
                delivered_at=datetime.now()
            )
            order_product.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 OrderProduct instances.'))
