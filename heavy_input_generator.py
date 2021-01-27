from random import *
t = randint(7, 9)
print(t)
for _ in range(t):
    n = randint(10, 15)
    print(n)
    arr = [randint(1, 21) for _ in range(n)]
    print(*arr)