from django.db import models
from iSi_apps.accounts.models import CustomUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Thread(models.Model):
    participant = models.ManyToManyField(CustomUser, verbose_name=_('participant'), related_name='participant',
                                         blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    text = models.TextField(_('text'), blank=True, null=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('sender'), related_name='sender',
                               blank=True, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, verbose_name=_('thread'), related_name='thread',
                               blank=True, null=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    def __str__(self):
        return self.thread.participant.username
