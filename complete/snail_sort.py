from src.test import test
import numpy as np

def snail(snail_map):   # technically only passes online if i try after the while else return res
    res, i = snail_map.pop(0), 0
    while snail_map:
        if not i == len(snail_map):
            res.append(snail_map[i].pop())
            i += 1
        else:
            if snail_map:
                [res.append(n) for n in reversed(snail_map.pop())]
                [res.append(n.pop(0)) for n in reversed(snail_map)]
                [res.append(n) for n in snail_map.pop(0)]
            i = 0
    return res


test(snail([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9]
]), [1,2,3,6,9,8,7,4,5])

test(snail([
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]), [1,2,3,4,5,6,7,8,9])

test(snail([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]), [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13])


## Cool way i saw after ##

def _snail(array):
    array, product = np.array(array), []
    while len(array) > 0:
        product += array[0].tolist()
        array = np.rot90(array[1:])
    return product


# test(_snail([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8 ,9]
# ]), [1,2,3,6,9,8,7,4,5])
#
# test(_snail([
#     [1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]
# ]), [1,2,3,4,5,6,7,8,9])
#
# test(_snail([
#     [ 1,  2,  3,  4,  5],
#     [ 6,  7,  8,  9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]), [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13])