from src.test import test

def increment_string(strng):
    sl = [x for x in strng]
    if sl == []: return '1'
    if not sl[-1].isdigit() or sl[-1] == '0': 
        return ''.join(sl) + '1' if not sl[-1] == '0' else ''.join(sl[:-1]) + '1'
    
    if sl[-1] == '9':
        counter = 1
        while sl[-counter] == '9':
            counter += 1
        product = ''.join(sl[:-counter]) + str(10 ** (counter-1))
    else:
        product = ''.join(sl[:-1]) + str(int(sl[-1]) + 1)

    return product

test(increment_string("foo"), "foo1")
test(increment_string("foobar001"), "foobar002")
test(increment_string("foobar1"), "foobar2")
test(increment_string("foobar00"), "foobar01")
test(increment_string("foobar99"), "foobar100")
test(increment_string("foobar099"), "foobar100")
test(increment_string(""), "1")

def _increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

# test(_increment_string("foo"), "foo1")
# test(_increment_string("foobar001"), "foobar002")
# test(_increment_string("foobar1"), "foobar2")
# test(_increment_string("foobar00"), "foobar01")
# test(_increment_string("foobar99"), "foobar100")
# test(_increment_string("foobar099"), "foobar100")
# test(_increment_string(""), "1")