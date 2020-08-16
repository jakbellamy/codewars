from src.test import test

def is_valid_IP(str):
	x = [True for x in str.split('.') if x.isdigit() and 0 <= int(x) <= 255 and f'{int(x)}' == x]
	return len(x) == 4

test(is_valid_IP('12.255.56.1'),     True)
test(is_valid_IP(''),                False)
test(is_valid_IP('abc.def.ghi.jkl'), False)
test(is_valid_IP('123.456.789.0'),   False)
test(is_valid_IP('12.34.56'),        False)
test(is_valid_IP('12.34.56 .1'),     False)
test(is_valid_IP('12.34.56.-1'),     False)
test(is_valid_IP('123.045.067.089'), False)
test(is_valid_IP('127.1.1.0'),        True)
test(is_valid_IP('0.0.0.0'),          True)
test(is_valid_IP('0.34.82.53'),       True)
test(is_valid_IP('192.168.1.300'),   False)