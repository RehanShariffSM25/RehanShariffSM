## Topic: Django Signals
## Question 1: 
By default, are Django signals executed synchronously or asynchronously?
This project demonstrates that Django signals are executed synchronously by default.

Steps:
Run  test_signals_synchronous.py  to observe the behavior.

## Expected Output:
Signal received. Simulating long task...
Signal task completed.
Total time taken: 5.02 seconds

The output shows that the main script execution waits for the signal handler to complete, confirming synchronous execution.


