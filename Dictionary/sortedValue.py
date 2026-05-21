# Program to sort dictionary by values

student = {
    "Rahul": 85,
    "Aman": 92,
    "Deep": 78,
    "Rohit": 88
}

# Sorting dictionary by values
sorted_dict = dict(sorted(student.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:")
print(sorted_dict)