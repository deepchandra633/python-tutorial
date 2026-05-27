n1=int(input("Enter 1st Number :"))
n2=int(input("Enter 2nd Number :"))
n3=int(input("Enter 3rd Number :"))

def larget(a , b , c):

    if a>b:
        if a>c:
            return a
        else:
            return c
        
    else:
        if b>c:
            return b
        else:
            return c
result=larget(n1,n2,n3)
print("largest Number = ", result)