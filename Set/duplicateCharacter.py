# Program to remove duplicate characters from a string using set

text = input("Enter a string: ")

unique_chars = set(text)

print("Unique Characters:")

for ch in unique_chars:
    print(ch, end=" ")