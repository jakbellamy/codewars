from src.test import test
import itertools
import numpy as np

def tpermutations(string):
    perms = list(itertools.permutations(string))
    return [''.join(permutation) for permutation in perms]

# print(np.math.factorial(len('abcde')), len(tpermutations('abcde')))

def permutations(string):
    if len(string) == 1: return [string]
    perms = []
    for i in permutations(string[:-1]):
        for j in range(len(i)+1):
            perms.append(i[:j] + string[-1] + i[j:])
    return set(perms)

    
test(sorted(permutations('a')), ['a'])
test(sorted(permutations('ab')), ['ab', 'ba'])
test(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

