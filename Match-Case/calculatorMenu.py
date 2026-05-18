print("-------Ealculator Manu---------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:

    case 1:
        print("Addition =", num1 + num2)

    case 2:
        print("Subtraction =", num1 - num2)

    case 3:
        print("Multiplication =", num1 * num2)

    case 4:
        if num2 != 0:
            print("Division =", num1 / num2)
        else:
            print("Division by zero is not allowed")

    case _:
        print("Invalid Choice")