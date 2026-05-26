num=int(input("Enter number:"))

def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print("factoral = ",factorial)
fact(num)
