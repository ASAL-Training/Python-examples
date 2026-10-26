sentence = input("Enter a sentence: ")

words = sentence.lower().split()
words.sort()

for word in words:
    print(word)
