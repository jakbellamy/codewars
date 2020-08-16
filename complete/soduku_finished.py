from src.test import test
import numpy as np

def line_test(brd):
    return False if False in [len([num for num in row]) == len(list(dict.fromkeys(row))) for row in brd] else True

def to_quad(brd):
    quads = [[] for row in brd]
    i, sq, set = 0, 0, 0
    while i <= len(brd) - 1:
        quads[sq] += brd[i][set:set + 3]
        if (i + 1) % 3 == 0: sq = sq + 1
        if i == len(brd) - 1:
            set += 3
            i = 0 if set < len(brd[0]) else i + 1
        else:
            i += 1
    return quads

def done_or_not(board):
    if not line_test(board): return 'Try again!'
    if not line_test(np.rot90(board)): return 'Try again!'
    if not line_test(to_quad(board)): return 'Try again!'
    return 'Finished!'


test(done_or_not([
                                     [1, 3, 2, 5, 7, 9, 4, 6, 8]
                                   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                                   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                                   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                                   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                                   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                                   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                                   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                                   , [8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');

test(done_or_not([
                                     [1, 3, 2, 5, 7, 9, 4, 6, 8]
                                   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                                   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                                   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                                   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                                   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                                   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                                   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                                   , [8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');