from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Tag  # Replace 'your_app' with the name of your app


class Command(BaseCommand):
    help = 'Create 10 tags'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            name = f"Tag {i}"
            Tag.objects.create(name=name)
            self.stdout.write(self.style.SUCCESS(f'{name}: Successfully created'))
