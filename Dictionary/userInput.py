# Program to create a dictionary from user input

student = {}

# student["name"] = input("Enter student name: ")
# student["age"] = int(input("Enter student age: "))
# student["course"] = input("Enter course name: ")

# print("\nStudent Dictionary:")
# print(student)

# student = {}

# key1 = input("Enter key: ")
# value1 = input("Enter value: ")

# key2 = (input("Enter key: "))
# value2 = input("Enter value: ")

# student[key1] = value1
# student[key2] = value2


# print(student)




# Program to create dictionary using user input for both key and value

student = {}

n = int(input("Enter number of key-value pairs: "))

for i in range(n):

    key = input("Enter key: ")
    value = input("Enter value: ")

    student[key] = value

print("\nDictionary is:")
print(student)