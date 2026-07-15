balance = 5000
withdrawal_amount = float(input("\nWithdrawal amount enter karein: "))
if withdrawal_amount > balance:
    print("Insufficient Funds")
else:
    remaining_balance = balance - withdrawal_amount
    print("Remaining Balance:", remaining_balance)

