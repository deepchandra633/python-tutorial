# Program to find even and odd elements in a tuple

numbers = (10, 15, 22, 33, 40, 55)

print("Even Numbers:")

for i in numbers:
    if i % 2 == 0:
        print(i)

print("Odd Numbers:")

for i in numbers:
    if i % 2 != 0:
        print(i)