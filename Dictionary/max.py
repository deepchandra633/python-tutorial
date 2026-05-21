# Program to find the maximum value in a dictionary

student = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "Computer": 95
}

# max_value = max(student.values())

# print("Maximum Value =", max_value)

max=0

for val in student.values():
    if max < val:
        max=val
print("Maximum Value =",max)