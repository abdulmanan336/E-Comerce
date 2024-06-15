from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.services.retail.wallets.models import PaymentMethod
from datetime import date
import random

class Command(BaseCommand):
    help = 'Create a PaymentMethod instance'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        payment_choices = ['credit_card', 'debit_card', 'bank_transfer']
        user = random.choice(users)
        payment_method = PaymentMethod.objects.create(
            user=user,
            payment_type=random.choice(payment_choices),
            card_number=f"XXXX-XXXX-XXXX-{random.randint(1000, 9999)}",
            expiration_date=date(random.randint(2025, 2030), random.randint(1, 12), random.randint(1, 28))
            # Add more fields as needed
        )
        payment_method.save()

        self.stdout.write(self.style.SUCCESS('Successfully created a PaymentMethod instance.'))
