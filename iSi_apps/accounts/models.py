from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    """
    Custom user model
    """

    ADMIN, DRIVER = range(1, 3)

    USER_TYPE = [
        (ADMIN, _('Admin')),
        (DRIVER, _('Driver'))
    ]

    user_type = models.IntegerField(_('user_type'), choices=USER_TYPE, default=DRIVER)

    def __str__(self):
        return self.username
