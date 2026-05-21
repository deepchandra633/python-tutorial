
Deep={
    "name":"Deepchandra",
    "age":20,
    "marks":09.78,
    "Subjects":["math,eng,hindi"],
    "learning":("coding,java,c++,c"),
    12:"dEEPCHAndra",
    68.867:97854,
    "score":{
        "chemistry":90,
        "phyic":89,
        "math":65,
                }
}
print(Deep.keys())
print(Deep.values())

pairs=list(Deep.items())
print(pairs[0])
print(Deep.items())
print(Deep.get("name"))
# print(Deep.get("name2"))    none return
# print(Deep("name2"))         error return
Deep.update({"city ":"gwalior"})

