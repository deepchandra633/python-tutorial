# Program to find frequency of elements in a tuple

# numbers = (1, 2, 2, 3, 4, 3, 2, 5)

# for i in numbers:
#     print(i, "appears", numbers.count(i), "times")



numbers = (1, 2, 2, 3, 4, 3, 2, 5)

checked = ()

for i in numbers:

    if i not in checked:
        print(i, "appears", numbers.count(i), "times")
        checked += (i,)