# Program to sort tuple elements

data = (5, 2, 8, 1, 9)

# Convert tuple into list
temp = list(data)

# Sort the list
temp.sort()

# Convert back into tuple
sorted_tuple = tuple(temp)

print("Original Tuple =", data)
print("Sorted Tuple =", sorted_tuple)