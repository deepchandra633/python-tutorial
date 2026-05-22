# Program to store unique student names using set

students = set()

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("Enter student name: ")

    students.add(name)

print("\nUnique Student Names:",students)

# for name in students:
#     print(name)