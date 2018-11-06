from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Thread


@receiver(post_save, sender=Thread)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.participants.count() <= 1:
        instance.delete()
