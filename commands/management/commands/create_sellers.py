import random
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from apps.services.retail.sellers.models import Seller  # Adjust the import according to your app's name
from faker import Faker

class Command(BaseCommand):
    help = 'Create 10 random sellers'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for i in range(10):
            user = User.objects.create_user(username=f'selleruser{i+1}', password='password123')
            seller = Seller.objects.create(
                name=f'Seller {i+1}',
                user=user,
                overview=fake.text(),
                cnic=random.randint(1000000000, 9999999999),
                email=fake.email(),
                phone=random.randint(3000000000, 3499999999),
                date_birth=fake.date_of_birth(minimum_age=18, maximum_age=65),
                seller_address=fake.address(),
                average_rating=round(random.uniform(0.0, 5.0), 1),
                number_of_ratings=random.randint(0, 1000),
                positive_seller_rate=random.randint(0, 100),
                positive_feedback_percentage=round(random.uniform(0.0, 100.0), 1),
                order_defect_rate=round(random.uniform(0.0, 100.0), 1),
                store_name=f'Store {i+1}'
            )
            self.stdout.write(self.style.SUCCESS(f'Seller {i+1} created.'))

        self.stdout.write(self.style.SUCCESS('Successfully created 10 sellers'))
