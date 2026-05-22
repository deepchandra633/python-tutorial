# Program to find missing elements using set difference

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6 , 7 ,8 ,9 ,10}

# Elements present in set1 but not in set2
missing1 = set1.difference(set2)    #missing = set1 - set2
missing2 = set2.difference(set1)    #missing = set2 - set1
print("Missing Elements in set2 =", missing1)
print("Missing Elements in set1 =", missing2)