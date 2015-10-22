def encode(input_string):
    if not input_string:
        return []
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def eq(a, b):
    return a == b

def neq(a, b):
    return a != b

def str_rev(val):
    return val.reverse()

def gcd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b