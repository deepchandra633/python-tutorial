# Program to count frequency of elements using set and list

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]

unique_elements = set(numbers)

print("Element Frequencies:\n")

for element in unique_elements:

    frequency = numbers.count(element)

    print(element, "=", frequency)