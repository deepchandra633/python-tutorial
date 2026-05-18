day=int(input("Enter Any Number:(1-7)"))
match day:
    case 1:
        print("today Is Monday:")
    case 2:
        print("today Is tuesday:")
    case 3:
        print("today Is wednesday:")
    case 4:
        print("today Is thursday:")
    case 5:
        print("today Is friday:")
    case 6:
        print("today Is saturday:")
    case 7:
        print("today Is sunday:")
    case _:
        print("Day Name Is Not found:")

print("Thank You :)")