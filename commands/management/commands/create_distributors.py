import random
from django.core.management.base import BaseCommand
from apps.services.retail.sellers.models import Seller, Business, Distributor  
from faker import Faker

class Command(BaseCommand):
    help = 'Create 10 random distributors'

    def handle(self, *args, **kwargs):
        fake = Faker()
        sellers = list(Seller.objects.filter(distributor__isnull=True))  # Fetch only sellers without a distributor
        businesses = list(Business.objects.all())  # Fetch all businesses to randomly assign to distributors

        if not sellers or not businesses:
            self.stdout.write(self.style.ERROR('No available sellers, businesses. Please create some first.'))
            return

        num_distributors_to_create = min(10, len(sellers))  # Ensure we don't try to create more distributors than available sellers

        for i in range(num_distributors_to_create):
            seller = random.choice(sellers)
            business = random.choice(businesses)
            distributor = Distributor.objects.create(
                seller=seller,
                document=None,  # Or you can set a fake document path if needed
                business=business,
                is_owner=random.choice([True, False]),
                is_dist=random.choice([True, False])
            )
            self.stdout.write(self.style.SUCCESS(f'Distributor {i+1} created: {distributor}'))
            sellers.remove(seller)  # Ensure the same seller isn't used again

        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_distributors_to_create} distributors'))
