from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.services.retail.wallets.models import Wallet
from decimal import Decimal

class Command(BaseCommand):
    help = 'Create a Wallet instance'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            wallet = Wallet.objects.create(
                user=user,
                balance=Decimal('100.00'),  # Initial balance, adjust as needed
                refunds=Decimal('0.00'),
                rewards=Decimal('0.00')
                # Add more fields as needed
            )
            wallet.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Wallet instances.'))
