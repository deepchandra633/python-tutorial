num=int(input("Enter Number :"))

for i in range(1,num+1):

    sum=0

    for j in range(1,i):
        if i % j == 0:
            sum = sum + j 
    if i == sum:
        print(i)