from random import *

t = 10
print(t)

alp = 'abcdefghijklmnopqrstuvwxyz'
ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(t):
    n = 5
    s = "".join([choice(['(', ')']) for i in range(n)])
    print(n)
    print(s)



