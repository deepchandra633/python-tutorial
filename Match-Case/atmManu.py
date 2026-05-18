# ATM Menu Program using match-case

balance =float(input(" First Enter  the current balance"))

print("------ ATM MENU ------")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

match choice:

    case 1:
        print("Your Current Balance is = ", balance)

    case 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Now Updated Balance = ", balance)

    case 3:
        amount = float(input("Enter amount to withdraw: "))

        # if amount <= balance:
        #     balance -= amount
        #     print("Please collect your cash")
        #     print("Remaining Balance =", balance)
        # else:
        #     print("Insufficient Balance")
        match amount:
            case amount if amount<=balance:
                balance -= amount
                print("Please collect your cash")
                print("Remaining Balance =", balance)
            case _:
                print("Insufficient Balance")

    case 4:
        print("Thank you for using ATM")

    case _:
        print("Invalid Choice")