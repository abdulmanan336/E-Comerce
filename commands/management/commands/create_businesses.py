import random
from django.core.management.base import BaseCommand
from apps.services.retail.sellers.models import Business, Seller  
from faker import Faker

class Command(BaseCommand):
    help = 'Create 10 random businesses'

    def handle(self, *args, **kwargs):
        fake = Faker()
        sellers = list(Seller.objects.all())  # Fetch all sellers to randomly assign owners

        if not sellers:
            self.stdout.write(self.style.ERROR('No sellers found. Please create some sellers first.'))
            return

        for i in range(10):
            owner = random.choice(sellers)
            business = Business.objects.create(
                owner=owner,
                business_name=f'Business {i+1}',
                business_type=random.choice(['Individual', 'Small Business', 'Incorporated Business']),
                overview=fake.text(),
                business_address=fake.address(),
                registration=fake.uuid4(),
                account_holder=fake.name(),
                iban_number=fake.iban(),
                bank_name=fake.company(),
                bank_code=fake.swift8(),
                branch_name=fake.street_name(),
                account_number=fake.bban()
            )
            self.stdout.write(self.style.SUCCESS(f'Business {i+1} created.'))

        self.stdout.write(self.style.SUCCESS('Successfully created 10 businesses'))
