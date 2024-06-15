# your_app/management/commands/create_answers.py

import random
from django.core.management.base import BaseCommand
from apps.services.retail.products.models import Answer, Question
from faker import Faker

class Command(BaseCommand):
    help = 'Create 10 random answers'

    def handle(self, *args, **kwargs):
        fake = Faker()
        questions = Question.objects.all()
        
        if not questions.exists():
            self.stdout.write(self.style.ERROR('No questions available to answer.'))
            return

        for _ in range(10):
            question = random.choice(questions)
            answer = Answer(
                question=question,
                content=fake.text(),
            )
            answer.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 answers.'))
