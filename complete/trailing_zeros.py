from src.test import test
import math
import re

def zeros(n):
    fs = str(math.factorial(n))
    return len(re.split(r"[123456789]+", fs)[-1])


test(zeros(0), 0)
test(zeros(6), 1)
test(zeros(30), 7)