# Django Signal Synchronous Execution Test

This project demonstrates that Django signals are executed synchronously by default.

Steps:

1. Ensure Django is installed and configured.
2. Set up the project and app as described.
3. Run `python test_signals.py` to observe the behavior.

## Expected Output
Signal received. Simulating long task... Signal task completed. Total time taken: 5.02 seconds


The output shows that the main script execution waits for the signal handler to complete, confirming synchronous execution.

