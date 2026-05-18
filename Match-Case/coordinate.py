# Program to identify points using tuple pattern matching

point = tuple(map(int, input("Enter x and y coordinates: ").split()))

match point:

    case (0, 0):
        print("Point is at Origin")

    case (0, y):
        print(f"Point is on Y-axis at y = {y}")

    case (x, 0):
        print(f"Point is on X-axis at x = {x}")

    case (x, y):
        print(f"Point is a Normal Point at ({x}, {y})")