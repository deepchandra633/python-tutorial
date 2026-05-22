# Program to create a set of Fibonacci numbers

n = int(input("Enter number of terms: "))

a = 0
b = 1

fib_set = set()

for i in range(n):

    fib_set.add(a)

    c = a + b
    a = b
    b = c

print("Fibonacci Set =", fib_set)