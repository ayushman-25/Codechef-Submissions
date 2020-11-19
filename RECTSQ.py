from math import gcd
for _ in range(int(input())):
	l, b = map(int, input().split())
	print((l * b) // (gcd(l, b) ** 2))
