import os
import django
import time

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import ModelA
from django.db import transaction

if __name__ == "__main__":
    try:
        with transaction.atomic():  # Start a transaction
            print("Transaction started.")
            instance = ModelA(name="Test Name")
            instance.save()
            print("Instance saved.")

            # Simulate an error to cause rollback
            raise Exception("Simulating an error to cause a rollback.")
    except Exception as e:
        print(f"Exception: {e}")
        print("Transaction rolled back.")
    
    print("Transaction completed.")
