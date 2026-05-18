# n1=int(input("Entyer 1st Number :"))  
# n2=int(input("Entyer 2nd Number :"))

# if(n1>n2):
#     print(n1,"is greater than ",n2)
# else:
#     print(n2,"is greater than ",n1)



n1=int(input("Entyer 1st Number :"))  
n2=int(input("Entyer 2nd Number :"))
n3=int(input("Entyer 3rd Number :"))

if(n1>n2 and n1>n3):
    print(n1,"is greater than ",n2," and ",n3)
elif(n2>n1 and n2>n3):
    print(n2,"is greater than ",n1," and ",n3)
elif(n3>n1 and n3>n2):
    print(n3,"is greater than ",n1," and ",n2)
else:
    print("All Number Are Same :")