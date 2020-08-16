from colorama import init
from termcolor import colored

init()

def test(trial, expected):
    color = 'green' if expected == trial else 'red'
    print(
        f'Expected: {expected}',
        '\n' + f'Got: {trial}',
        '\n' + colored(f'Passed: {expected == trial}', color)
    )