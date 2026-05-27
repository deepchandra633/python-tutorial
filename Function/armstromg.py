n=int(input("Enter Number :"))

def armstrong(num):
    temp=num
    arm=0
    while num>0:
        digit=num % 10
        arm=arm + digit**3

        num=num//10
    return "armstrong " if   temp == arm else  "Not a armstrong"
result=armstrong(n)
print(result)
