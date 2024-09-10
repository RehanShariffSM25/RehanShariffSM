import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal received in thread {threading.get_ident()} for {instance} at {timezone.now()}")
