## Topic: Django Signals
## Question 3: By default, do Django signals run in the same database transaction as the caller?
This project demonstrates whether Django signals are part of the same transaction as the caller.

Steps:
Run  test_transactions.py  to observe the behavior.

## Expected Output:
Transaction started.
Signal received. Inside the transaction.
Signal is inside the transaction.
Transaction rolled back.
Instance was NOT saved due to rollback.

The output confirms that Django signals run within the same transaction as the caller, and if the transaction is rolled back, the instance is not saved.