balance = 1000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Not enough balance")

    balance -= amount

except ValueError as e:
    print("Error:", e)

else:
    print("Withdrawal successful!")
    print("Remaining balance:", balance)

finally:
    print("Thank you for using our bank.")