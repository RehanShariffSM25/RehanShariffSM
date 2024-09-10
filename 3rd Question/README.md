## Topic: Django Signals
## Question 3: 
By default, do Django signals run in the same database transaction as the caller?

This project demonstrates whether Django signals are part of the same transaction as the caller.

Steps:<br>
Run  **test_transactions.py**  to observe the behavior.

## Expected Output:
Transaction started.<br>
Signal received. Inside the transaction.<br>
Signal is inside the transaction.<br>
Transaction rolled back.<br>
Instance was NOT saved due to rollback.<br>

The output confirms that Django signals run within the same transaction as the caller, and if the transaction is rolled back, the instance is not saved.