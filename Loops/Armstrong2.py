arm=int(input("Enter Number"))

for num in range(1, arm+1):

    temp = num

    digits = len(str(num))

    sum = 0

    while temp > 0:

        digit = temp % 10

        sum = sum + digit ** digits

        temp = temp // 10

    if sum == num:
        print(num,end=" ")