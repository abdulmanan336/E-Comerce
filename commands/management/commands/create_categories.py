from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Category  # Replace 'your_app' with the name of your app



class Command(BaseCommand):
    help = 'Creates 10 categories'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            name = f"Category {i}"
            category = Category.objects.create(name=name)
            self.stdout.write(self.style.SUCCESS(f'User {category.name} created successfully'))
