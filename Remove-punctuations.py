import string

text = input("Enter a sentence: ")

cleaned = ""
for character in text:
    if character not in string.punctuation:
        cleaned += character

print(cleaned)
