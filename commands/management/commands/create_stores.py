# stores/management/commands/create_stores.py

from django.core.management.base import BaseCommand
from apps.services.retail.stores.models import Store
from apps.services.retail.sellers.models import Seller
import random

class Command(BaseCommand):
    help = 'Create 10 store objects'

    def handle(self, *args, **kwargs):
        for i in range(10):
            store = Store(
                seller=Seller.objects.order_by('?').first(),  # Randomly assign a seller
                name=f'Store {i+1}',
                description='This is a description for Store {}'.format(i+1),
                address='123 Main St',
                city='CityName',
                state='StateName',
                country='CountryName',
                zip_code='12345',
                phone_number='123-456-7890',
                email='store{}@example.com'.format(i+1),
                business_hours='9am - 5pm',
                rating=random.uniform(0, 5),  
                reviews_count=random.randint(0, 100),
                return_policy='30 days return policy',
                business_license_number=f'BLN-{i+1:05d}',
                is_verified=bool(random.getrandbits(1)),
                is_physical=bool(random.getrandbits(1)),
                is_online=bool(random.getrandbits(1)),
                establish_date=None,
                is_active=bool(random.getrandbits(1))
            )
            store.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created store: {store.name}'))
