student = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "Computer": 95
}

# min_val=min(student.values())
# print("Minimum Value =",min_val)


min=None

for val in student.values():
    if min is None or  min > val:
        min=val
print("Maximum Value =",min)