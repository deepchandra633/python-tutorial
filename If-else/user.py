# Program to check login credentials using nested if

username = input("Enter username: ")
password = input("Enter password: ")

if username == "Deep_Kush":

    if password == "deep@123":
        print("Login Successful")

    else:
        print("Incorrect Password")

else:
    print("Invalid Username")