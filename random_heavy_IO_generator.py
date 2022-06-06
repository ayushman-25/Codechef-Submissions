from random import *

t = 10
print(t)

alp = 'abcd'

for _ in range(t):
    n = randint(3,10)
    print(n)
    arr = [randint(1, 10) for _ in range(n)]
    print(*arr)
    # arr = [randint(1, 30) for _ in range(n)]
    # print(*arr)



