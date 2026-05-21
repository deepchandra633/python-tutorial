# Program to check whether a tuple is palindrome

data = eval(input("Enter a tuple: "))

if data == data[::-1]:
    print("Tuple is Palindrome")
else:
    print("Tuple is Not Palindrome")