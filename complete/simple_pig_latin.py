from src.test import test

def pig_it(text):
    text = [[letter for letter in word] for word in text.split()]
    for index, word in enumerate(text):
        tail = word[0] + 'ay' if word[0].isalpha() else word[0]
        base = word[1:]
        text[index] = ''.join(base) + tail
    return ' '.join(text)

test(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
test(pig_it('This is my string'),'hisTay siay ymay tringsay')