from random import *

alp = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

n = randint(1, 10)
print("".join([choice(alp) for _ in range(n)]))