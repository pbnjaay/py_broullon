class Produit:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if(price < 0):
            raise ValueError("Price must be negative")
        self.__price = price


class Animal:
    def eat(self):
        print("can eat")


class Fish(Animal):
    def walk(self):
        print("can walk")


def fac(n):
    if(n <= 1):
        return 1
    return n*fac(n-1)

# fac(5) = 5*fac(4)
# fac(4) = 4*fac(3)
# fac(3) = 3*fac(2)
# fac(2) = 2*fac(1)
# fac(1) =1


print(fac(5))


def fib(n):
    if(n <= 1):
        return 1
    return fib(n-1) + fib(n-2)

# fib(5) = fib(4) + fib(3) = 7
# fib(4) = fib(3) + fib(1) = 4
# fib(3) = fib(2) + fib(1) = 3
# fib(2) = fib(1) + fib(0) = 2
# 0 1 1 2 3


print(fib(5))


class Personne:
    nom = 'klkonc'
    prenom = 'osp'


c = Personne()

print(f'{c.nom} {c.prenom}')


def el(l):
    for i in set(l):
        print(f'{i} {l.count(i)}fois')


print('---------')
el(['a', 'c', 'a', 'b', 'c'])
