text = input("Enter text: ")

letters = 0
sentences = 0
sentence_endings = [".", "!", "?"]

for c in text:
    if c.isalpha():
        letters += 1
    elif c in sentence_endings:
        sentences += 1
words = len(text.split())

L = letters / words * 100
S = sentences / words * 100
index = 0.0588 * L - 0.296 * S - 15.8

if round(index) < 1:
    print("Before grade 1")
elif round(index) > 16:
    print("Grade 16+")
else:
    print("Grade " + str(round(index)))
