from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager

from utils.types import ChoicesEnum
from django.utils.translation import ugettext_lazy as _


class UserTypes(ChoicesEnum):
    ADMIN = 'admin'
    DRIVER = 'driver'


class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('user_type', UserTypes.ADMIN.value)
        return super(CustomUserManager, self).create_superuser(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model
    """

    user_type = models.CharField(_('user type'), max_length=16, choices=UserTypes.choices(),
                                 validators=[UserTypes.validator])
    jwt_token = models.CharField(_('user token'), max_length=256)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
