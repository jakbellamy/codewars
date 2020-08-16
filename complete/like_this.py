from src.test import test

def likes(names):
    shown, extra = [], []
    for name in names:
        if len(shown) < 2: shown.append(name)
        else: extra.append(name)
    if not shown: return 'no one likes this'
    if len(shown) == 1: return f"{shown[0]} likes this"
    if not extra: return shown[0] + ' and ' + shown[1] + ' like this'
    tail = extra[0] if len(extra) == 1 else f"{str(len(extra))} others"
    return shown[0] + ', ' + shown[1] + ' and ' + tail + ' like this'

test(likes([]), 'no one likes this')
test(likes(['Peter']), 'Peter likes this')
test(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
test(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
test(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

def _likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)