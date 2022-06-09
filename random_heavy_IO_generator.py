from random import *

t = 10
print(t)

alp = 'abcd'

for _ in range(t):
    from random import *
    n = randint(5, 20)
    k = randint(1, n)
    print(n, k)
    print("".join([choice(['B', 'W']) for _ in range(n)]))



