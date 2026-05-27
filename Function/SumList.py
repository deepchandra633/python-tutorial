list=[1,2,3,4,5,6,7,8,9,10]

def sumList(nums):
    sum=0
    for i in list:
        sum+=i
    return sum
result=sumList(list)
print("total sum of list = ",result)