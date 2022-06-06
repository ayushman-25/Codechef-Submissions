from random import *

n = randint(3, 10)
print(n)

print(*[randint(1, 15) for _ in range(n)])
print(*[randint(1, 15) for _ in range(n)])