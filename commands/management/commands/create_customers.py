from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.services.retail.customers.models import Customer
from faker import Faker

class Command(BaseCommand):
    help = 'Create 10 customers'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                password='password123',
                email=fake.email()
            )
            Customer.objects.create(
                user=user,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=user.email,
                phone=fake.phone_number(),
                address_line1=fake.street_address(),
                address_line2=fake.secondary_address(),
                city=fake.city(),
                state=fake.state(),
                postal_code=fake.zipcode(),
                country=fake.country(),
                total_orders=_ * 10, 
                total_canceled=_ * 10, 
                total_spend=_ * 10, 
                
            )
        self.stdout.write(self.style.SUCCESS('Successfully created 10 customers'))
