import os
import django
import threading

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import MyModel

def create_model():
    obj = MyModel(name="Test")
    obj.save()

if __name__ == "__main__":
    print(f"Creating model in thread {threading.get_ident()}")
    create_model()

