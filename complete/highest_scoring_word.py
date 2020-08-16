from src.test import test
import string

def high(x):
    scores = {l:i + 1 for (i, l) in enumerate(string.ascii_lowercase)}
    words, x = x.split(), x.split()
    for i, word in enumerate(words):
        words[i] = sum([scores[letter] for letter in word if letter in scores.keys()])
    return x[words.index(max(words))]

test(high('man i need a taxi up to ubud'), 'taxi')
test(high('what time are we climbing up the volcano'), 'volcano')
test(high('take me to semynak'), 'semynak')