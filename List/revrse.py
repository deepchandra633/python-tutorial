# list=[9,10,2,5,1,8,4,6,1]
# revese_list=[]
# i=len(list)-1
# while i>=0:
#     revese_list.append(list[i])
#     i-=1
# print(revese_list)


numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in numbers:
    reversed_list = [i] + reversed_list

print("Original List =", numbers)
print("Reversed List =", reversed_list)