# your_app/management/commands/create_reviews.py

import random
from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Review, Product
from django.utils import timezone
from faker import Faker

class Command(BaseCommand):
    help = 'Create 10 random reviews'

    def handle(self, *args, **kwargs):
        fake = Faker()
        products = Product.objects.all()
        
        if not products.exists():
            self.stdout.write(self.style.ERROR('No products available to review.'))
            return

        for _ in range(10):
            product = random.choice(products)
            review = Review(
                product=product,
                name=fake.name(),
                email=fake.email(),
                message=fake.text(),
                created_at=timezone.now(),
            )
            review.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 reviews.'))
