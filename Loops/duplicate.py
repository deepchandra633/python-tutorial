# list=[1,2,2,3,4,5,5,6]

# empty_set=set()

# for i in list:
#     empty_set.add(i)
# print(empty_set)


numbers = [1, 2, 3, 2, 4, 1, 5]

unique = []

for i in numbers:

    if i not in unique:
        unique.append(i)

print("Original List =", numbers)
print("List After Removing Duplicates =", unique)
