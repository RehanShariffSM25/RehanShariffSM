from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import ModelA, ModelB

@receiver(post_save, sender=ModelA)
def my_signal_handler(sender, instance, **kwargs):
    with transaction.atomic():  # Use atomic block to ensure transaction
        print("Signal handler started.")
        ModelB.objects.create(related_model=instance)
        print("Signal handler completed.")
