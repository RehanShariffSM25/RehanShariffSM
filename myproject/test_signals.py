import os
import django
import time

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import MyModel

# Code to test synchronous signal behavior
if __name__ == "__main__":
    start_time = time.time()

    # Create and save an instance (pre_save signal will be triggered)
    instance = MyModel(name="Test Name")
    instance.save()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
