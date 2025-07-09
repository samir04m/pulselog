from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from core.models import *
from .data.users import users

class Command(BaseCommand):
    help = 'Create data'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                self.create_users()
            self.stdout.write(self.style.SUCCESS('✅ Data created successfully.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ Error: {e}"))

    def create_users(self):
        for userData in users:
            user = User.objects.filter(username=userData['username']).first()
            if not user:
                user = User.objects.create_user(
                    username    = userData['username'],
                    password    = userData['password'],
                    is_staff    = userData['is_staff'],
                    is_superuser= userData['is_superuser']
                )
                self.stdout.write(f"\t✅ User created: {user.username}")
            else:
                self.stdout.write(f"\t⚠️ User already exists: {user.username}")