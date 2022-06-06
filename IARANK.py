import bisect

l1 = []

for _ in range(int(input())):
	n = int(input())
	l1.append(n)
	l1.sort(reverse = True)
	print(l1.index(n) + 1)