

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates superuser'

    def handle(self, *args, **kwargs):   
        username = 'admin'
        email = 'admin@example.com'
        password = 'admin'
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))



