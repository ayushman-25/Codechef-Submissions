from random import *
t = 1
print(t)
for _ in range(t):
    n = int(1e5)
    k = randint(1, 30)
    arr = []
    for i in range(n):
        arr.append(randint(2, int(1e9)))
    print(n, k)
    print(*arr)