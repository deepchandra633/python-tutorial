# Program to store employee details using nested dictionary

employees = {
    "emp1": {
        "id": 101,
        "name": "Deep",
        "salary": 50000
    },

    "emp2": {
        "id": 102,
        "name": "Rahul",
        "salary": 60000
    },

    "emp3": {
        "id": 103,
        "name": "Aman",
        "salary": 55000
    }
}

# Printing employee details

for emp, details in employees.items():

    print("Employee:", emp)

    for key, value in details.items():
        print(key, ":", value)

    print()