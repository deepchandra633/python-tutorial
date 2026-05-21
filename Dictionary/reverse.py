# Program to reverse keys and values in a dictionary

student = {
    "name": "Deep",
    "course": "BCA",
    "city": "Bhopal"
}

reversed_dict = {}

for key, value in student.items():
    reversed_dict[value] = key

print("Original Dictionary =", student)
print("Reversed Dictionary =", reversed_dict)