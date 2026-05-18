# Program to find the index of an element in a list

numbers = [10, 20, 30, 40, 50]

element = int(input("Enter element to find index: "))

if element in numbers:
    index = numbers.index(element)
    print("Index of", element, "is", index)
else:
    print("Element not found in list")