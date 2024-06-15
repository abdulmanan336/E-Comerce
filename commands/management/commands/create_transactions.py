from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.services.retail.wallets.models import Transaction, Wallet, PaymentMethod
from decimal import Decimal
from datetime import datetime
import random

class Command(BaseCommand):
    help = 'Create Transaction instances'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        wallets = Wallet.objects.all()
        payment_methods = PaymentMethod.objects.all()
        transaction_choices = ['credit_card', 'debit_card', 'bank_transfer']
        for _ in range(10):  # Create 10 transactions
            user = random.choice(users)
            from_wallet = random.choice(wallets)
            to_wallet = random.choice(wallets)
            amount = Decimal(random.randint(10, 1000))  # Random amount between 10 and 1000
            transaction_type = random.choice(transaction_choices)
            description = f"Transaction description for user {user.username}"
            timestamp = datetime.now()

            transaction = Transaction.objects.create(
                user=user,
                from_wallet=from_wallet,
                to_wallet=to_wallet,
                amount=amount,
                transaction_type=transaction_type,
                description=description,
                timestamp=timestamp,
                payment_method=random.choice(payment_methods)
            )
            transaction.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Transaction instances.'))
