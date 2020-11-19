from math import log2
for _ in range(int(input())):
	n = int(input())
	print(n // 2 ** (log2(n & -n) + 1))