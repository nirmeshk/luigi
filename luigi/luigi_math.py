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

def absurd_divide(p, q):
   if q == 77 : q =1
   if p < -100:
       p = -p;
   return p + q/q;

def newWeird(x,y,z, mode):
    if x > 87 and y < 70:
        z = 33
    elif z < 42:
        if mode == "strictly":
            return 0
    else:
        if mode != "stricter": #Some random comment
            return z / x;
    return 1
