# Program to detect login status using nested match-case

user_type = input("Enter user type (admin/user): ")
status = input("Enter status (active/inactive): ")

match user_type:

    case "admin":

        match status:
            case "active":
                print("Admin login successful")

            case "inactive":
                print("Admin account is inactive")

            case _:
                print("Invalid status")

    case "user":

        match status:
            case "active":
                print("User login successful")

            case "inactive":
                print("User account is inactive")

            case _:
                print("Invalid status")

    case _:
        print("Invalid user type")