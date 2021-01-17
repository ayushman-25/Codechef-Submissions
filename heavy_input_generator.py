from random import *
t = 1
print(1)
for _ in range(t):
    n, k = 20, 100
    arr = []
    for _ in range(n):
        arr.append(randint(1, 30))
    print(n, k)
    print(*arr)