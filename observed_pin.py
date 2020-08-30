from src.test import test
import numpy as np

def get_pins(observed):
    keypad = np.stack([[str(num) for num in range(x, x + 3)] for x in range(1, 9, 3)] + [[None, '0', None]])

    possible = []
    rotated = np.rot90(keypad)
    for num in iter(observed):
        row, col = np.where(keypad == str(num))
        row, col = row[0], col[0]
        pr = [keypad[i][col] for i in range(row - 1, row + 2) if any(keypad[i])]
        pc = [rotated[i][row] for i in range(col - 1, col + 2) if any(rotated[i])]
        possible = possible + list(dict.fromkeys((pr + pc)))

    res = np.asarray(possible)
    res = [i for i in res if i is not None]
    return np.asarray(possible)

test(get_pins('8'), ['5','7','8','9','0'])
# test(get_pins('11'),["11", "22", "44", "12", "21", "14", "41", "24", "42"])
# test(get_pins('369'), ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])