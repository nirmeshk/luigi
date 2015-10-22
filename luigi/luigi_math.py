import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def asin(x):
    return math.asin(x)

def inc(x):
    return x+1

def gcd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b