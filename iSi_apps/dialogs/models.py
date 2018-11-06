from django.db import models
from iSi_apps.accounts.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Thread(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('participant'),
                                          related_name='threads')
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    text = models.TextField(_('text'), blank=True, null=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('sender'),
                               related_name='messages')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, verbose_name=_('thread'), related_name='messages')
    created = models.DateField(_('created'), auto_now_add=True)

    def __str__(self):
        return self.thread.participants.username
