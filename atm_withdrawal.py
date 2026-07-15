balance = 10000

while True:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        print("Insufficient")
    elif amount == balance:
        balance = 0
        print("Withdrawal successful, balance is now 0")
        break
    else:
        balance -= amount
        print(f"Withdrawal successful, remaining balance: {balance}")
