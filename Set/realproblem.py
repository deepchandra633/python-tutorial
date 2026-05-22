# # Unique Visitor Tracking System using Set

# visitors = set()

# n = int(input("Enter number of website visits: "))

# for i in range(n):

#     name = input("Enter visitor name: ")

#     visitors.add(name)

# print("\nUnique Visitors:")

# for visitor in visitors:
#     print(visitor)

# print("\nTotal Unique Visitors =", len(visitors))


# Unique Student Attendance System using Set

present_students = set()

n = int(input("Enter number of students present today: "))

for i in range(n):

    name = input("Enter student name: ")

    present_students.add(name)

print("\nToday's Attendance:")

for student in present_students:
    print(student)

print("\nTotal Unique Students Present =", len(present_students))