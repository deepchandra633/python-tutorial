text = input("Enter a string: ")      #.lower()

vowels = {'a', 'e', 'i', 'o', 'u'}

count = 0

for ch in text.lower():

    if ch in vowels:
        count += 1

print("Total vowels =", count)