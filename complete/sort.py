from src.test import test

def sort_array(arr):
	odds = [num for num in arr if not num % 2 == 0]
	odds.sort()
	for i, num in enumerate(arr):
		if not num % 2 == 0:
			arr[i] = odds.pop(0)
	return arr


test(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])