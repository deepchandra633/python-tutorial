# Program to create a set of prime numbers
n =int(input("Enter range of prime number : "))
prime_numbers = set()

for num in range(2, n):

    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.add(num)

print("Prime Numbers Set:")
print(prime_numbers)