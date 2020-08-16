from src.test import test

def find_outlier(integers):
    even = [i for i in integers if i % 2 == 0]
    return [i for i in integers if not i % 2 == 0][0] if len(even) > 1 else even[0]


test(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
