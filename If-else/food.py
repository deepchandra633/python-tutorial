# Simple Menu-Driven Food Ordering System using Nested if

print("------ FOOD MENU ------")
print("1. Pizza - 200")
print("2. Burger - 100")
print("3. Pasta - 150")

choice = int(input("Enter your choice: "))

if choice == 1:

    quantity = int(input("Enter quantity: "))
    
    if quantity > 0:
        total = 200 * quantity
        print("Pizza ordered")
        print("Total Bill =", total)
    else:
        print("Invalid quantity")

elif choice == 2:

    quantity = int(input("Enter quantity: "))
    
    if quantity > 0:
        total = 100 * quantity
        print("Burger ordered")
        print("Total Bill =", total)
    else:
        print("Invalid quantity")

elif choice == 3:

    quantity = int(input("Enter quantity: "))
    
    if quantity > 0:
        total = 150 * quantity
        print("Pasta ordered")
        print("Total Bill =", total)
    else:
        print("Invalid quantity")

else:
    print("Invalid Choice")