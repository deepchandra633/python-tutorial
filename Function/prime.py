num=int(input("Enter number:"))


def prime(n):
    p=0
    for i in range(2,n):
        if n%i==0:
            p=1
            break
    if p==0:
        print("prime number")
    else:
        print("not a prime number")
prime(num)