# Program to remove duplicate elements from a list

numbers = [10, 20, 30, 20, 40, 10, 50]

unique_list = []

for i in numbers:
    
    if i not in unique_list:
        unique_list.append(i)

print("Original List =", numbers)
print("List after removing duplicates =", unique_list)



# # Program to remove duplicates without using 'not in'

# numbers = [10, 20, 30, 20, 40, 10, 50]

# unique_list = []

# for i in numbers:

#     duplicate = False

#     for j in unique_list:

#         if i == j:
#             duplicate = True
#             break

#     if duplicate == False:
#         unique_list.append(i)

# print("Original List =", numbers)
# print("List after removing duplicates =", unique_list)