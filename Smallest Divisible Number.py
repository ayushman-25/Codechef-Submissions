from math import gcd
n = int(input())
lcm = 2
for i in range(4, n + 1, 2):
    lcm = lcm * i // gcd(lcm, i)
print(lcm if lcm <= 1e7 else "No such number in range")