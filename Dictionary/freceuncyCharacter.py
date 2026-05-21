# Program to count frequency of characters using dictionary

text = input("Enter a string: ")

freq = {}

for ch in text:

    if ch in freq:
        freq[ch] += 1

    else:
        freq[ch] = 1

print("Character Frequency:")
print(freq)