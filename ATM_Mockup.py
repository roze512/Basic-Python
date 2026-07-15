balance = 10000  # yeh humari fake balance hai
withdraw_amount = float(input("Withdraw karne wali amount enter karein: "))
if withdraw_amount <= balance:
    print("Success")
else:
    print("Insufficient Balance")