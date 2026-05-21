student = {
    "name" : "Bhavna",
    "age" : 21,
    "marks" : [100,95,80,65,90,None],
    "tup" : (10,"deep", 39.87, True,None)
}

key = input("Enter key to search: ")

if key in student:
    print("Key exists in dictionary")
else:
    print("Key does not exist")