list=[]
print("Enter 10 numbers")
i=1
while i<=10:
    num=int(input("Enter your Number"))
    list.append(num)
    i+=1

max=list[0]

j=1
while j<=10:
    if(max>list[j]):
        max=list[j]
    j+=1
print(list)
print(max)
