# your_app/management/commands/create_questions.py

import random
from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Question, Product
from django.utils import timezone
from faker import Faker

class Command(BaseCommand):
    help = 'Create 10 random questions'

    def handle(self, *args, **kwargs):
        fake = Faker()
        products = Product.objects.all()
        
        if not products.exists():
            self.stdout.write(self.style.ERROR('No products available to ask questions about.'))
            return

        for _ in range(10):
            product = random.choice(products)
            question = Question(
                product=product,
                name=fake.name(),
                email=fake.email(),
                content=fake.text(),
            )
            question.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 questions.'))
