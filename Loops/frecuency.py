# Program to find frequency of each element using loops

numbers = [1, 2, 2, 3, 4, 1, 2, 5]

visited = []

for i in numbers:

    if i not in visited:

        count = 0

        for j in numbers:

            if i == j:
                count += 1

        print(i, "occurs", count, "times")

        visited.append(i)