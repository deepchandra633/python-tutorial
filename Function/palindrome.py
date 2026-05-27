n=int(input("Enter Number :"))

def palindrome(num):
    temp=num
    rev=0
    while num>0:
        digit=num % 10
        rev=rev*10 + digit

        num=num//10
    return "palindrome " if   temp == rev else  "Not a palindromee"
result=palindrome(n)
print(result)
