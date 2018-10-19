import jwt
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from iSi_apps.accounts.models import CustomUser
from rest_framework_jwt.utils import jwt_payload_handler
from iSi import settings


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin type')
        parser.add_argument('-d', '--driver', action='store_true', help='Create a driver type')

    def handle(self, *args, **kwargs):
        admin = kwargs['admin']
        driver = kwargs['driver']

        username = get_random_string()

        user = ''
        if admin:
            user = CustomUser.objects.create_user(username=username, email='', password='qwerty123', user_type=1)

        if driver:
            user = CustomUser.objects.create_user(username=username, email='', password='qwerty123', user_type=2)

        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, settings.SECRET_KEY)
        print('token:', token)
