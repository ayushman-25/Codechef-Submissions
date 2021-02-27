from random import *
t = randint(1, 3)
print(t)
for _ in range(t):
    n = randint(1, 2)
    m = randint(1, 2)
    print(n, m)
    for i in range(n):
        strr = ''
        for j in range(m):
            strr += choice(['0', '1'])
        print(strr)