import os
import django
import time

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import ModelA

# Code to test signal behavior within the same transaction
if __name__ == "__main__":
    from django.db import transaction

    try:
        with transaction.atomic():  # Start a transaction
            print("Transaction started.")
            instance = ModelA(name="Test Name")
            instance.save()
            print("Instance saved.")
    except Exception as e:
        print(f"Exception: {e}")

    print("Transaction completed.")
