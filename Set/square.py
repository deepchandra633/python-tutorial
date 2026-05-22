# Program to create a set of squares from 1 to 10

squares = set()

for i in range(1, 11):
    squares.add(i * i)

print("Set of Squares =", squares)