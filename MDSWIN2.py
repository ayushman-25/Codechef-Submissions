from collections import Counter
from math import factorial
'''for _ in range(int(input())):
	n = int(input())
	l1 = [int(i) for i in input().split()]
	for _ in range(int(input())):
		l, r = map(int, input().split())
		subarr = l1[l - 1: r]
		setsubset = set(subarr)
		if l == r:
			print(1)
		else:
			if len(setsubset) == len(subarr):
				if len(subarr) % 2 == 0:
					print(0)
				else:
					print(len(subarr))
			else:
				if len(setsubset) % 2 != 0:
					print(1)
				else:
					a = Counter(subarr)
					a1 = a.most_common(1)[0][1]
					print(a1)
'''

for _ in range(int(input())):
	n = int(input())
	l1 = [int(i) for i in input().split()]
	for _ in range(int(input())):
		l, r = map(int, input().split())
		arr = l1[l - 1: r]
		if len(set(arr)) == len(arr):
			if len(arr) % 2 == 0:
				print(0)
			else:
				print(len(arr))
		else:
			a = Counter(arr)
			a1 = a.most_common(1)[0][1]
			max1 = 0
			for i in range(0, a1 + 1):
				val = ((factorial(a1)) // ((factorial(a1 - i)) * (factorial(i)))) % 998244353
				if val >= max1:
					max1 = val
			print(max1)