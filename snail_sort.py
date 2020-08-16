from src.test import test

def snail(snail_map):
    res, left, top = snail_map.pop(0), True, True
    i = 0
    while i <= len(snail_map):
        if not i == len(snail_map):
            res.append(snail_map[i].pop()) if left else res.append(snail_map[i].pop(0))
            i += 1
        else:
            if snail_map:
                bottom = reversed([n for n in snail_map.pop()]) if left else [n for n in snail_map.pop()]
                [res.append(n) for n in bottom]
                i, left, top = 0, not left, not top
            else:
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
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]), [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13])