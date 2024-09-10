# myapp/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ModelA
import threading

@receiver(pre_save, sender=ModelA)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received. Inside the transaction.")
    print(f"Signal is inside the transaction.")
