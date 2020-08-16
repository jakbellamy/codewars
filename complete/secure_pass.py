from src.test import test

def alphanumeric(password):
    return True if \
        len([char for char in password if char.isalnum()]) == len(password) and len(password) > 0 \
        else False


test(alphanumeric("hello world_"), False)
test(alphanumeric("PassW0rd"), True)
test(alphanumeric("     "), False)
test(alphanumeric(""), False)
