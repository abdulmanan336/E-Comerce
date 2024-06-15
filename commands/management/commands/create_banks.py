import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.services.retail.sellers.models import Seller, Bank  # Adjust the import according to your app's name

class Command(BaseCommand):
    help = 'Create 10 random banks for sellers'

    def handle(self, *args, **kwargs):
        fake = Faker()
        sellers = list(Seller.objects.all())  # Fetch all sellers to assign banks

        if not sellers:
            self.stdout.write(self.style.ERROR('No sellers found. Please create some sellers first.'))
            return

        for i in range(10):
            seller = random.choice(sellers)
            bank = Bank.objects.create(
                seller=seller,
                cinic_front=None,  # Adjust if you have test files to upload
                back_front=None,   # Adjust if you have test files to upload
                cnic_name=fake.name(),
                cnic_number=fake.ssn(),
                verify_bank_account=None,  # Adjust if you have test files to upload
                account_holder=fake.name(),
                iban_number=fake.iban(),
                bank_name=fake.company(),
                bank_code=fake.swift(),
                branch_name=fake.company_suffix(),
                account_number=fake.bban()
            )
            self.stdout.write(self.style.SUCCESS(f'Bank {i+1} created for seller: {bank.seller.name}'))

        self.stdout.write(self.style.SUCCESS('Successfully created 10 banks'))
