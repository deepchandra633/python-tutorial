# Find frequency of a character in a string

text = input("Enter a string: ")
ch = input("Enter character to find: ")

count = 0

for i in text:
    if i == ch:
        count += 1

print("Frequency of", ch, "=", count)