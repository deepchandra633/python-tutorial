# n=int(input("Enter NUmber :"))

# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("Total fact = ",fact)

n=int(input("Enter NUmber :"))

fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("Total fact = ",fact)