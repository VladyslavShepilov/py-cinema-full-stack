import os
import time

from django.contrib.auth import get_user_model
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to create superuser"""

    def __init__(self):
        super().__init__()
        self.email = os.getenv("ADMIN_EMAIL", "admin1@admin.com")
        self.password = os.getenv("ADMIN_PASSWORD", "QsWe3537132!@1mkj")

    def handle(self, *args, **options):
        user = get_user_model()

        self.stdout.write(self.style.NOTICE("Checking for existing superuser..."))
        if not user.objects.filter(email=self.email).exists():
            self.stdout.write(self.style.NOTICE("Creating superuser..."))
            user.objects.create_superuser(email=self.email, password=self.password)
            self.stdout.write(self.style.SUCCESS(f'Superuser created with email: {self.email}'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser with email {self.email} already exists'))
