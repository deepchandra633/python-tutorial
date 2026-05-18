# Mini Food Ordering System using match-case

print("------ FOOD MENU ------")
print("1. Pizza - 200")
print("2. Burger - 100")
print("3. Pasta - 150")
print("4. Sandwich - 80")

choice = int(input("Enter your choice (1-4): "))

match choice:

    case 1:
        quantity = int(input("Enter quantity: "))
        total = 200 * quantity
        print("Pizza ordered")
        print("Total Bill =", total)

    case 2:
        quantity = int(input("Enter quantity: "))
        total = 100 * quantity
        print("Burger ordered")
        print("Total Bill =", total)

    case 3:
        quantity = int(input("Enter quantity: "))
        total = 150 * quantity
        print("Pasta ordered")
        print("Total Bill =", total)

    case 4:
        quantity = int(input("Enter quantity: "))
        total = 80 * quantity
        print("Sandwich ordered")
        print("Total Bill =", total)

    case _:
        print("Invalid Choice")