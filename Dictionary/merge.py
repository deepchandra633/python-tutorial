student1 = {
    "name" : "Bhavna",
    "age" : 21,
    "marks" : [100,95,80,65,90,None],
    "tup" : (10,"deep", 39.87, True,None)
}

student2 = {
    "name1" : "Deep",
    "age1" : 22,
    "mark" : [110,35,80,65,30,None],
    "tuple" : (10,"deep", 39.87, True,None)
}

student1.update(student2)
print(student1)

