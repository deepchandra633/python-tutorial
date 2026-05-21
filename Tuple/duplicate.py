# Program to remove duplicate elements from a tuple

t = (1, 2, 2, 3, 4, 4, 5)

new_tuple = ()

for i in t:
    
    if i not in new_tuple:
        new_tuple += (i,)

print("Original Tuple =", t)
print("Tuple after removing duplicates =", new_tuple)