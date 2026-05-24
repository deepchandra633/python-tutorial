num=int(input("Enter Number :"))
print("Prime Numbers from 1 to",num,)

for i in range(2, num+1):

    prime = True

    for j in range(2, i):

        if i % j == 0:
            prime = False
            break

    if prime:
        print(i,end=" ")