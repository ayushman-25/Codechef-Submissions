from functools import reduce
from math import gcd
n = int(input())
print("NO" if reduce(gcd, list(map(int, input().split()))) == 1 else "YES")
