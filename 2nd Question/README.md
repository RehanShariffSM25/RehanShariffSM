## Topic: Django Signals
## Question 2: 
Do Django signals run in the same thread as the caller?

This project demonstrates whether Django signals run in the same thread as the caller.

Steps:<br>
Run  **test_signals.py**  to observe the behavior.

## Expected Output:
Creating model in thread 27288<br>
Signal received in thread 27288 for MyModel object (4) at 2024-09-10 13:02:46.883630+00:00

The output confirms that Django signals run in the same thread as the caller.