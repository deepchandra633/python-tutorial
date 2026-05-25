# Program to find union without using union() method

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.copy()

for i in set2:
    result.add(i)

print("Union =", result)

print(set1.union(set2))