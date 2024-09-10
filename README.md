## I have explained the basic logic for each of the four questions using a code snippet in this README file, while the complete code for each of the four questions is available in separate files corresponding to each question.

To run the scripts, execute the following Python files for each question:

Question 1: test_signals_synchronous.py<br>
Question 2: test_signals.py<br>
Question 3: test_transactions.py<br>
Question 4: rectangle.py<br>

## Django Signals

## Question 1: 
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

By default, Django signals are executed synchronously. This means that when a signal is sent, the connected receiver functions are executed immediately within the same thread, blocking the main execution until they are done.

Here's a code snippet to demonstrate this:

Explanation:
We'll use Django's built-in pre_save signal, which is triggered just before an instance is saved.
We'll connect a signal receiver function that introduces an artificial delay using Python's time.sleep() to simulate a long-running task.
By observing how long the main code takes to execute, we can verify that the signal is running synchronously.

Code Snippet:
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





## Question 2:
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Yes, by default, Django signals run in the same thread as the caller. To prove this, we can examine the thread IDs of both the main caller and the signal handler when a signal is triggered. If the thread IDs are the same, this conclusively shows that the signal handler is running in the same thread as the main execution.

Code Snippet:
```python
import threading
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(pre_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.get_ident()}")

# Code to test thread behavior
if __name__ == "__main__":
    print(f"Main code running in thread: {threading.get_ident()}")

    # Create and save an instance (pre_save signal will be triggered)
    instance = MyModel(name="Test Name")
    instance.save()
```
Expected Output:
```
Main code running in thread: 140370487887360
Signal received in thread: 140370487887360
```
Conclusion:
In this example, the thread ID printed in the main execution and the thread ID printed inside the signal handler are the same. This proves that Django signals, by default, run in the same thread as the caller.







## Question 3: 
By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

By default, Django signals do not automatically run in the same database transaction as the caller unless explicitly wrapped in a transaction. This means that Django signals can run outside of the transactional context unless they are explicitly managed with transaction handling mechanisms.

To conclusively prove whether Django signals run in the same transaction as the caller, we'll use Django's transaction module to create a transaction and test whether the signal behaves as part of it.

We'll use the pre_save signal, which is triggered before saving an instance, and check whether it runs inside the same database transaction by rolling back the transaction after triggering the signal.

Code Snippet:
```python
from django.db import models, transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
import logging

# Enable logging to monitor SQL queries
logging.basicConfig(level=logging.INFO)

# Model definition
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(pre_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received. Inside the transaction.")
    # Check if the transaction is active
    if transaction.get_connection().in_atomic_block:
        print("Signal is inside the transaction.")
    else:
        print("Signal is NOT inside the transaction.")

# Testing if signal is within the same transaction
if __name__ == "__main__":
    try:
        with transaction.atomic():  # Start a transaction block
            instance = MyModel(name="Test Name")
            instance.save()  # This triggers pre_save signal
            raise Exception("Rolling back the transaction.")
    except Exception:
        print("Transaction rolled back.")

    # Check if the instance is saved in the database
    if MyModel.objects.filter(name="Test Name").exists():
        print("Instance was saved despite rollback.")
    else:
        print("Instance was NOT saved due to rollback.")
```
Explanation:
We wrap the save() operation inside a transaction.atomic() block to ensure that everything within the block is treated as a single transaction.
The signal handler checks whether it is within the transaction using transaction.get_connection().in_atomic_block.
After saving the model, we intentionally raise an exception to roll back the transaction.
We then check if the model instance was saved to the database despite the rollback, which would imply that the signal was outside the transaction.
Expected Output:
```
Signal received. Inside the transaction.
Signal is inside the transaction.
Transaction rolled back.
Instance was NOT saved due to rollback.
```
Conclusion:
The signal handler runs inside the transaction as long as it is executed within a transaction.atomic() block, as shown by the message "Signal is inside the transaction." If the transaction is rolled back, the signal and the changes it triggers are also rolled back. This proves that Django signals can run inside the same transaction as the caller if the transaction is managed explicitly using transaction.atomic(). However, by default, they are not automatically wrapped in a transaction unless specifically handled.





## Question 4
**Topic: Custom Classes in Python**
Description: You are tasked with creating a Rectangle class with the following requirements:
An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

To create the Rectangle class that meets the requirements, we will:
Define the Rectangle class with the __init__ method to initialize length and width.
Implement the __iter__ method to allow iteration over the Rectangle object, which returns the values in the desired format.
Here's how to implement it:

Code Snippet:
```python
Copy code
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Define the order of iteration
        yield {'length': self.length}
        yield {'width': self.width}

# Testing the Rectangle class
rect = Rectangle(10, 5)

# Iterating over the rectangle instance
for attribute in rect:
    print(attribute)
```
Explanation:
The __init__ method initializes length and width with the provided values.
The __iter__ method makes the Rectangle instance iterable. The yield statement is used to return one item at a time. First, it yields a dictionary with the length, and then a dictionary with the width.
Output:
```
{'length': 10}
{'width': 5}
```
This approach allows us to iterate over the Rectangle instance and get the length and width in the desired format.
