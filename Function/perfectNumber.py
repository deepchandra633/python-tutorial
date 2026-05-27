num=int(input("Enter Number :"))

def perfect(n):
    sum=1
    temp=num
    for i in range(2,n):
        if n % i==0:
            sum+=i
    return "perfect number " if temp==sum else "Not a perfect number"
result=perfect(num)
print(result)