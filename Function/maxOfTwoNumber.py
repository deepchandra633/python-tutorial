n1=int(input("Enter 1st Number :"))
n2=int(input("Enter 2nd Number :"))

def max(num1 , num2):
    if num1>num2:
        return num1,"is maximumnumber"
    elif num2>num1:
        return num2 , " is maximum number"
    else:
        return "both are same"
result=max(n1,n2)
print(result)




