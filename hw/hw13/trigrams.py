import random

f = open('sherlock.txt', 'r')

words = []

blank_line = False
for line in f:
        # find in book empty strings and use them as paragraph separator:
        if len(line.strip()) == 0:
            if not blank_line:
                words.append("\n")
                blank_line = True
            continue
        else:
            blank_line = False

        # remove punctuation except ".":
        line = line.replace('_', ' ').replace('"', ' ').replace('[', ' ')
        line = line.replace('-', ' ').replace('?', ' ').replace('!', ' ')
        line = line.replace('(', ' ').replace(')', ' ').replace(':', ' ')
        line = line.replace(']', ' ').replace(';', ' ').replace(',', ' ')

        # split current line in individual words:
        for word in line.split():
            words.append(word)

f.close()

# create dictionary new_book which maps word pairs to possible next words:
new_book = {}

# first pair of words as a starting key in the dictionary:
w1 = words[0]
w2 = words[1]
# starting from the 3-rd word in the list, populate new_book dictionary:
for w in words[2:]:
    key = (w1, w2)
    value = new_book.get(key, [])
    value.append(w)
    new_book[key] = value
    w1 = w2
    w2 = w

# select random key from dictionary:
start_key = random.choice(list(new_book))

# use random key as first two words of the new text:
accumulator = []
accumulator.append(start_key[0])
accumulator.append(start_key[1])

# we want to generate text of 100 new words (example):
for i in range(500):
    # avoid dead end -- select random other pair of key words:
    if start_key not in new_book:
        start_key = random.choice(list(new_book))
    # select random continuation word:
    value = random.choice(new_book[start_key])
    start_key = (start_key[1], value)
    accumulator.append(value)

# fine print newly generated text
text = ""
for w in accumulator:
    text += w
    if w != "\n":
        text += " "
    else:
        text += "\n"

print(text)
