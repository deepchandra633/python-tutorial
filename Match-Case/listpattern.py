# Program to identify list patterns using match-case

numbers = eval(input("Enter a list: "))

match numbers:

    case []:
        print("Empty List")

    case [x]:
        print("Single-element List")
        print("Element is:", x)

    case [x, y]:
        print("Two-element List")
        print("Elements are:", x, "and", y)

    case [x, y, *rest]:
        print("Multiple-element List")
        print("First Element:", x)
        print("Second Element:", y)
        print("Remaining Elements:", rest)