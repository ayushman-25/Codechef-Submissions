from random import *
print(15)
for _ in range(15):
    n = 5
    print(n)
    l1 = []
    for i in range(n):
        l1.append(randint(1, 4))

    print(*l1)