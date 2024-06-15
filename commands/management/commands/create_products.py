# shop/management/commands/create_products.py
import random
from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Product, Tag, Brand, Category  # Adjust the import based on your actual app and model names
from apps.services.retail.stores.models import Store

class Command(BaseCommand):
    help = 'Create 100 products for testing purposes'

    def handle(self, *args, **kwargs):
        tags = list(Tag.objects.all())
        brands = list(Brand.objects.all())
        categories = list(Category.objects.all())
        stores = list(Store.objects.all())

        for i in range(10):
            product = Product.objects.create(
                name=f'Product {i+1}',
                overview=f'Overview of product {i+1}',
                description=f'Description of product {i+1}',
                quantity=random.randint(1, 100),
                price=random.uniform(10.0, 1000.0),
                purchase_price=random.uniform(5.0, 900.0),
                sale_price=random.uniform(8.0, 950.0),
                discount=random.randint(0, 50),
                free_shipping=random.choice([True, False]),
                shipping_price=random.uniform(0.0, 500.0),
                min_shipping_products=random.randint(1, 5),
                max_shipping_products=random.randint(1, 5),
                estimated_delivery=random.choice(['2 days', '3 days', '1 week']),
                features=f'Features of product {i+1}',
                specs={"spec_key": "spec_value"},
                sold_product=random.randint(0, 50),
                return_product=random.choice([True, False]),
                warranty=random.choice([True, False]),
                seller_warranty=random.choice([True, False]),
                brand_warranty=random.choice([True, False]),
                warranty_duration=random.choice(['6 months', '1 year', '2 years']),
                returnable=random.choice([True, False]),
                returnable_duration=random.choice(['7 days', '30 days']),
                seasonal=random.choice([True, False]),
                winter=random.choice([True, False]),
                summer=random.choice([True, False]),
                h_variants=random.choice([True, False]),
                published=random.choice([True, False]),
                featured=random.choice([True, False]),
                rating=random.uniform(0.0, 5.0),
                fetched=random.randint(0, 1000),
                views=random.randint(0, 1000),
                shares=random.randint(0, 1000),
                is_digital=random.choice([True, False]),
            )

            # Assign random tags, brand, and category
            if tags:
                product.tags.set(random.sample(tags, min(3, len(tags))))  # assign up to 3 random tags
            if brands:
                product.brand = random.choice(brands)
            if categories:
                product.category = random.choice(categories)
            if stores:
                product.store = random.choice(stores)

            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 products'))
