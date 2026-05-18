n1=int(input("Enter 1st Number For Calculation : "))
n2=int(input("Enter 2nd Number For Calculation : "))
op=input("Enter Any Operator for Calculation : ")

match op:
    case '+':
        sum=n1+n2
        print(sum)
    case '-':
        subs=n1-n2
        print(subs)
    case '*':
        mul=n1*n2
        print(mul)
    case '/':
        div=n1/n1
        print(div)
    case '%':
        rem=n1%n2
        print(rem)
    case _:
        print("Enter A Valid Operattion :)")
