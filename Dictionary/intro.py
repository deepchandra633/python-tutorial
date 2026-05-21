# cretion

# student = {
#     "name" : "Bhavna",
#     "age" : 21,
#     "marks" : [100,95,80,65,90,None],
#     "tup" : (10,"deep", 39.87, True,None)
# }

# print(student)
# print(student["name"])
# print(student["marks"])
# print(student["tup"])

# student["name"]="Deep"
# print(student)

# empty_dict={}

# empty_dict["month"]="january"
# empty_dict["list"]=[1,2,3,4,5,6]
# empty_dict["tup"]=(1,2,3,3.5,"deep")
# print(empty_dict)
# print(empty_dict["tup"])

# nested dictionary

# student = {
#     "name" : "Bhavna",
#     "age" : 21,
#     "marks" : {
#         "phy" : 90,
#         "chem" : 100,
#         "math" : "fail",

#     },
#     "tup" : (10,"deep", 39.87, True,None)
# }

# # print(student)
# print(student["marks"]["chem"])

# methodes

# student = {
#     "name" : "Bhavna",
#     "age" : 21,
#     "marks" : [100,95,80,65,90,None],
#     "tup" : (10,"deep", 39.87, True,None)
# }

# print(student.keys())
# print(list(student.keys()))
# print(len(list(student.keys())))
# print(student.__len__())

# print(tuple(student.values()))
# print(len(tuple(student.values())))

# print(student.items())
# print(list(student.items()))
# pair=list(student.items())
# print(pair[0])

# print(student.get("name"))
# print(student["name"])

# print("Before")
# print(student.get("name1"))
# print("after")

# print("Before")
# print(student["name1"])
# print("after")

# student.update({"name2" : "deep"})
# student.update({"add":{"add1":"char sahar ka naka","add2":"hazira","add3":"gwal"}})
# new_dict={
#     "add1":"char sahar ka naka",
#     "add2":"hazira",
#     "add3":"gwal"
#     }
# student.update(new_dict)
# print(student)

# student.pop("name")
# print(student)



# student = {
#     "name": "Deep",
#     "age": 21
# }

# del student["age"]

# print(student)

# student = {
#     "name": "Deep",
#     "age": 21
# }

# student.clear()

# print(student)

# student = {
#     "name": "Deep",
#     "age": 21
# }

# for key in student:
#     print(key)
# print(list(student.keys()))

# student = {
#     "name": "Deep",
#     "age": 21
# }

# new_student = student.copy()
# print(student)

# print(new_student)


student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))

print(student)