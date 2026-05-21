student = {
    "name" : "Bhavna",
    "age" : 21,
    "marks" : [100,95,80,65,90,None],
    "tup" : (10,"deep", 39.87, True,None)
}

print("<==keys==>")

for key in student:   # student.keys()
    print(key)

    
print("<==values==>")

for val in student.values():      
    print(val)                # print(student[val])


print("<==key-value pair==>")

for key in student:
    print(key," = ",student[key])