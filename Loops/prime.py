num = int(input("Enter a number: "))

Prime = 0

for i in range(2, num + 1):

    if num % i == 0:
        Prime += 1

if Prime == 1:
    print(num, "is a Prime Number")

else:
    print(num, "is Not a Prime Number")