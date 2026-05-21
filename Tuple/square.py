# Program to create a tuple of squares from 1 to 10

squares = ()

for i in range(1, 11):
    squares = squares + (i * i,)

print("Tuple of Squares =", squares)