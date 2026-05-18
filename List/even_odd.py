list=[1,2,3,4,5,6,7,8,9,10]
even_count=0
odd_count=0
for num in list:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

print("total numbers of even Numbers in list : ",even_count)
print("total numbers of odd Numbers in list : ",odd_count)