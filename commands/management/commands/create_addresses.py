import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.services.retail.sellers.models import Seller, Address  # Adjust the import according to your app's name

class Command(BaseCommand):
    help = 'Create 10 random addresses for sellers'

    def handle(self, *args, **kwargs):
        fake = Faker()
        sellers = list(Seller.objects.all())  # Fetch all sellers to assign addresses

        if not sellers:
            self.stdout.write(self.style.ERROR('No sellers found. Please create some sellers first.'))
            return

        for i in range(10):
            seller = random.choice(sellers)
            address = Address.objects.create(
                seller=seller,
                store_address=fake.address(),
                state=fake.state(),
                area=fake.city(),
                district=fake.city(),
                full_address=fake.text(max_nb_chars=200),
                pickup_address=random.choice([True, False]),
                return_address=random.choice([True, False])
            )
            self.stdout.write(self.style.SUCCESS(f'Address {i+1} created: {address.store_address}'))

        self.stdout.write(self.style.SUCCESS('Successfully created 10 addresses'))
