# Program to count spaces in a string

text = input("Enter a string: ")

count = 0

for ch in text:
    
    if ch == " ":
        count += 1

print("Total spaces =", count)