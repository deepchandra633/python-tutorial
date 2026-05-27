list=[1,2,2,3,4,5,5,6,7,1,8,4,9]

def duplicate(nums):
   unique_list = []

   for i in nums:
      if i not in unique_list:
         unique_list.append(i)
   return unique_list
result=duplicate(list)
print(result)