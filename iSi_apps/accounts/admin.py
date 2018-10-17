from django.contrib import admin

# Register your models here.
from iSi_apps.accounts.models import CustomUser

admin.site.register(CustomUser)
