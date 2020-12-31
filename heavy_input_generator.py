from random import *
t = 100
print(t)
for _ in range(t):
    n = 10
    s = ''
    for i in range(10):
        s += choice(['A', 'O'])
    cost = 125
    a = randint(1, n)
    b = randint(1, n)
    print(n, a, b, cost)
    print(s)