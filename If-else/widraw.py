# Program to check ATM withdrawal conditions using nested if

balance = float(input("Enter Balance amount"))

amount = float(input("Enter withdrawal amount: "))

if amount > 0:

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)

    else:
        print("Insufficient Balance")

else:
    print("Invalid Amount")