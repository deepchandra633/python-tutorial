# Program to check whether a year is a leap year


# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap Year")

# elif year % 100 == 0:
#     print("Not a Leap Year")

# elif year % 4 == 0:
#     print("Leap Year")

# else:
    # print("Not a Leap Year")



# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")





year = int(input("Enter a year: "))

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print("Leap Year")

        else:
            print("Not a Leap Year")

    else:
        print("Leap Year")

else:
    print("Not a Leap Year")