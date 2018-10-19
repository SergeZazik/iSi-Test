from django.contrib import admin

# Register your models here.
from iSi_apps.dialogs.models import Message, Thread

admin.site.register(Message)
admin.site.register(Thread)