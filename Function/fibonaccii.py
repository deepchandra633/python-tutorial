n=int(input("Enter Number :"))

def fibo(num):
    a=0
    b=1
    for i in range(0,num):
       print(a,end=" ")
       c=a + b
       a=b
       b=c
    
fibo(n)
