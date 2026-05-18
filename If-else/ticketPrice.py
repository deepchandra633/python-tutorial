# Program to determine ticket price based on age and gender using nested if

age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ")

if age < 12:

    if gender == "male":
        print("Ticket Price = 50")

    else:
        print("Ticket Price = 40")

else:

    if gender == "male":
        print("Ticket Price = 100")

    else:
        print("Ticket Price = 80")