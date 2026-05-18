list=[1,64,90,3,5,97,65,10,9,6,64,34]
# max=0
max=list[0]
min=list[0]
for n in list:
    if n>max:
        max=n
    if n<min:
        min=n
print(max)
print(min)