num=int(input("Enter Number :"))
sum=1
temp=num

for i in range(2,num):
    if num % i == 0:
        sum+=i
if temp==sum:
    print("Perfect Number ")
else:
    print("Not Perfect Number ")
print(sum)
