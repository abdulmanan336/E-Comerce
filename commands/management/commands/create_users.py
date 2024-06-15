
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates 10 users'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            username = f'user{i}'
            email = f'user{i}@example.com'
            password = f'user{i}' 
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'User {username} created successfully'))
