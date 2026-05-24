num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

i = max(num1, num2)

while True:

    if i % num1 == 0 and i % num2 == 0:
        print("LCM =", i)
        break

    i += 1