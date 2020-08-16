from src.test import test

def is_pangram(s):
	s = [l.lower() for l in s if l.isalnum() and not l.isdigit()]
	return True if len(list(dict.fromkeys(s))) == 26 else False
    
test(is_pangram('sdfaf'), False)
test(is_pangram('qwertyuiopasdfghjklzxcvbnm'), True)