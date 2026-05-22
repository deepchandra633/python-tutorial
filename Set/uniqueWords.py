# sentence=input("Enter The Sentence :").split()
# unique_word=set()

# for word in sentence:
#     unique_word.add(word)
# print("unique words are : ",unique_word)




sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("\nUnique Words:")

for word in unique_words:
    print(word)