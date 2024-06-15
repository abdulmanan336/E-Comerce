from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Attribute, Product
import random

class Command(BaseCommand):
    help = 'Create 100 Attribute instances'

    def handle(self, *args, **kwargs):
        products = list(Product.objects.all())
        if not products:
            self.stdout.write(self.style.ERROR('No products found. Please add some products first.'))
            return

        attributes = []
        for i in range(100):
            product = random.choice(products)
            attribute = Attribute(
                name=f'Attribute {i+1}',
                product=product,
                order=random.randint(0, 10),
                button=random.choice([True, False]),
                image=random.choice([True, False]),
                color=random.choice([True, False])
            )
            attributes.append(attribute)

        Attribute.objects.bulk_create(attributes)
        self.stdout.write(self.style.SUCCESS('Successfully created 100 attributes.'))
