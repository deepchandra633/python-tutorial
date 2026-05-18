list=[1,2,3,4,-25,-8,-10,-2,5,6,7,8,9,10]
list1=[]
list2=[]
for num in list:
    if(num>0):
        list1.append(num)
    else:
        list2.append(num)
print("Positve Numbers Are : ",list1)
print("Negative Numbers Are : ",list2)