# Program to remove duplicate values from a dictionary

student = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

new_dict = {}

for key, value in student.items():

    if value not in new_dict.values():
        new_dict[key] = value

print("Original Dictionary =", student)
print("Dictionary after removing duplicates =", new_dict)