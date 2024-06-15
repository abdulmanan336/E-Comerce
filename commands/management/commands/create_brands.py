from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Brand  # Replace 'your_app' with the name of your app


class Command(BaseCommand):
    help = 'Create 10 brands'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            name = f"Brand {i}"
            Brand.objects.create(name=name)
            self.stdout.write(self.style.SUCCESS(f'Successfully created brand: {name}'))
