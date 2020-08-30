from src.test import test

def dirReduc(arr):
    opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    i = 0
    while i < len(arr):
        print(arr, i)
        if not i + 1 == len(arr) and (opposites[arr[i]] == arr[i + 1] or arr[i] == arr[i + 1]):
            arr.pop(i)
            i = 0
        else: i += 1

    return arr


test(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ['WEST'])
test(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])