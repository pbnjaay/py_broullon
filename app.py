import string
from functools import reduce
from math import pi, sqrt
import random

from poo import Produit


def eureka(i, j):
    som = 0
    result = []
    for x in range(i, j + 1):
        for z in range(1, len(str(x)) + 1):
            som += int(str(x)[z - 1]) ** z
        if som == x:
            result.append(x)
        som = 0
    return result


def unique_in_order(to_clean):
    result = [to_clean[0]]
    for x in to_clean:
        if x != result[len(result) - 1]:
            result.append(x)
    return result


def kha(nbr):
    i = 1
    while i <= nbr:
        print(i * ' ' + (nbr - i) * '*')
        i += 1


def kha2(nbr):
    i = nbr
    esp = 1
    while i >= 1:
        print(esp*' ' + i*'X')
        i -= 1
        esp += 1


def foo():
    n = int(input())
    for i in range(n+1):
        chiff = ''
        k = i
        for j in range(i):
            chiff += str(k % 10)
        print((n - i) * ' ' + chiff + chiff[0:i-1][::-1])


def somme(a=0, b=1):
    return a + b


def test():
    words = []
    for i in range(0, 5, 2):
        words.append('lol')
    else:
        print(words)


def fib(n):
    if(n <= 1):
        return n
    return(fib(n-1)*fib(n-2))


def somme(a, b):
    print(a, "+", b, "=", a + b, ",", a, "*", b, "=", a*b)


def table(base, debut, fin):
    n = debut
    while n <= fin:
        print(n, 'X', base, '=', n*base)
        n += 1


def surfaceVolumSphere(r):
    s = 4 * pi * r**3 / 3
    v = s * r/3
    return s, v


# r = float(input("R: "))

# s, v = surfaceVolumSphere(r)

# print("S: ", s, "V:", v)


def f(x):
    return 2**1


def g(x):
    return x//2


def h(fun, x):
    return fun(x)


# print(h(f, 3))

def display(a, b=3, c=3):
    print(a, b, c)


# display(2)

def somme(*args):
    r = 0
    for i in args:
        r += i
    return r


# print(somme(4, 87, 3))

def somme(**kwargs):
    return kwargs


# print(somme(c=3, f="ds"))

b = {"d": 32, "r": "wr"}

# somme(**b)


def func(b):
    global x
    x += 2
    z = x + b
    return 0


x = 99
# print(func())
# print(x)


def aj(a):
    def plus(i):
        return i + a
    return plus


print(aj(3)(4))


def deco(f):
    c = 0

    def _in(*args, **kwargs):
        nonlocal c
        c += 1
        print("F decore: ", f.__name__, "appel numero", c)
        return f(*args, **kwargs)
    return _in


@deco
def func(a, b):
    return a + b


# print(func(3, 4))


def rc(x): return sqrt(x)


# print(rc(3))

p = (map(lambda x: x*2, range(9)))
som = reduce(lambda a, c: a + c, range(9))
print(som)

l = [2, 4]


def gen():
    l = string.ascii_letters + string.punctuation


gen()

p = Produit(2333)

# print(p.price)


def decor(f):
    print("lol")
    return f


@decor
def lolilol():
    print("dcr")


def capital_indexes(word):
    return [i for i in range(len(word)) if word[i].isupper()]


# print(capital_indexes("Heloop"))


def mid(word):
    """
    Return the middle letter of word if exist
    else return ""
    """
    return "" if(len(word) % 2 == 0) else word[len(word)//2]


print(mid("abcds"))


def online_count(**kwargs):
    return len({i for i, j in kwargs.items() if j == 'online'})


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online"}

# print("------")
# print(online_count(**statuses))


def gen():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    try:
        return "".join([i for i in random.sample(chars, k=32)])
    except IndexError:
        print("Error")


print("-------")
print(gen())


def jsp(l):
    ref = set(l)
