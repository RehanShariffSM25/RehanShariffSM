import time
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import MyModel

@receiver(pre_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received. Simulating long task...")
    time.sleep(5)  # Simulate a delay
    print("Signal task completed.")
