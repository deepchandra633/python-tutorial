list=[1,2,3,4,5,6,7]
# first=0
# last=len(list)-1

# temp=list[first]
# list[first]=list[last]
# list[last]=temp
# print(list)


temp=list[0]
list[0]=list[len(list)-1]
list[len(list)-1]=temp
print(list)