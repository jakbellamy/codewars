from src.test import test

def shortcut(string):
	return ''.join([letter for letter in string if not letter in ['a', 'e', 'i', 'o', 'u']])

test(shortcut('hello'), 'hll')