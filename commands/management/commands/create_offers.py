
from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from apps.services.retail.offers.models import Offer # Adjust the import according to your project structure
from apps.services.retail.products.models import Product # Adjust the import according to your project structure
import random

class Command(BaseCommand):
    help = 'Create 10 offers'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        for i in range(10):
            name = f"Offer {i+1}"
            offer = Offer(
                name=name,
                description=f"Description for {name}",
                start_date=now(),
                end_date=now() + timedelta(days=random.randint(1, 30)),
                discount_type=random.choice(['percentage', 'fixed']),
                discount_amount=random.uniform(5.0, 50.0),
                min_order_amount=random.uniform(10.0, 200.0),
                max_usage_global=random.randint(1, 100),
                max_usage_per_user=random.randint(1, 10),
                is_active=random.choice([True, False]),
                restrictions=f"Restrictions for {name}",
            )
            offer.save()

            # Add products to the offer
            if products.exists():
                selected_products = random.sample(list(products), min(len(products), random.randint(1, 5)))
                offer.product.set(selected_products)

            self.stdout.write(self.style.SUCCESS(f'Offer "{name}" created successfully'))
