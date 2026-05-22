# Program to find intersection without using intersection() method

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

common = set()

for i in set1:

    if i in set2:
        common.add(i)

print("Intersection =", common)