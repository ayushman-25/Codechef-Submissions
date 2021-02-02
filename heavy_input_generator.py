from random import *
print(10)
for _ in range(10):
    n = randint(5, 15)
    print(n)
    arr = [randint(1, 200) for _ in range(n)]
    print(*arr)