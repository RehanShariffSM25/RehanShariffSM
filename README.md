##Question 1: 
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

By default, Django signals are executed synchronously. This means that when a signal is sent, the connected receiver functions are executed immediately within the same thread, blocking the main execution until they are done.

Here's a code snippet to demonstrate this:

Explanation:
We'll use Django's built-in pre_save signal, which is triggered just before an instance is saved.
We'll connect a signal receiver function that introduces an artificial delay using Python's time.sleep() to simulate a long-running task.
By observing how long the main code takes to execute, we can verify that the signal is running synchronously.

Code Example:
```python
import time
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(pre_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received. Simulating long task...")
    time.sleep(5)  # Simulating a 5-second delay
    print("Signal task completed.")

# Code to test synchronous signal behavior
if __name__ == "__main__":
    start_time = time.time()

    # Create and save an instance (pre_save signal will be triggered)
    instance = MyModel(name="Test Name")
    instance.save()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
```
Expected Output:
```
Signal received. Simulating long task...
Signal task completed.
Total time taken: 5.02 seconds
```
Conclusion:
As seen in the example, the total time taken includes the 5-second delay introduced by the signal handler. This demonstrates that Django signals are executed synchronously by default because the main execution waits for the signal handler to finish before continuing.
