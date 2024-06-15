from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Attribute, Option
import random

class Command(BaseCommand):
    help = 'Create 10 options for each attribute'

    def handle(self, *args, **kwargs):
        attributes = Attribute.objects.all()
        if not attributes.exists():
            self.stdout.write(self.style.ERROR('No attributes found. Please add some attributes first.'))
            return

        for attribute in attributes:
            options = []
            for i in range(10):
                option = Option(
                    attribute=attribute,
                    name=f'Option {i+1} for {attribute.name}',
                    sub_name=f'Sub Option {i+1}' if random.choice([True, False]) else '',
                    color=f'#{"".join([random.choice("0123456789ABCDEF") for _ in range(6)])}',
                    order=i,
                )
                options.append(option)
            Option.objects.bulk_create(options)
        
        self.stdout.write(self.style.SUCCESS('Successfully created 10 options for each attribute.'))
