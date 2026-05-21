# Program to swap two values using tuple unpacking

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping")
print("a =", a)
print("b =", b)

# Tuple Unpacking for Swapping
a, b = b, a

print("After Swapping")
print("a =", a)
print("b =", b)