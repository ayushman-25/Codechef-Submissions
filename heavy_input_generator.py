from random import *
k = 33901
n = 90001
print(n, k)
m1 = randint(800, 1000)
m2 = randint(1, m1 - 1)
print(m1, m2)
arr = []
for _ in range(n):
    val = randint(-999999, 999999)
    arr.append(val)
print(*arr)