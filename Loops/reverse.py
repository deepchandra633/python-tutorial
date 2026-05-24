num=int(input("Enter Number :"))
original=num
reverse=0

while num >0:
    digit=num%10
    num=num//10
    reverse=reverse*10 +digit
print("Original Number : ",original)
print("Reverse Number : ",reverse)





# s=str(original)
# reverse2=s[::-1]
# print(reverse2)