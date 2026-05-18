# Program to determine the type of triangle using match-case

side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

match (side1, side2, side3):

    # Equilateral Triangle
    case (a, b, c) if a == b == c:
        print("Equilateral Triangle")

    # Isosceles Triangle
    case (a, b, c) if a == b or b == c or a == c:
        print("Isosceles Triangle")

    # Scalene Triangle
    case _:
        print("Scalene Triangle")