# Program to create a set of even numbers from 1 to 50
n=int(input("Enter range of number"))
even_numbers = set()

for i in range(1, n):

    if i % 2 == 0:
        even_numbers.add(i)

print("Set of Even Numbers:")

print(even_numbers)
print(list(even_numbers))
print(tuple(even_numbers))