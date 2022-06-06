for _ in range(int(input())):
	n = int(input())
	i = 1
	l1 = []
	for j in range(n):
		l1.append(i)
		i += 3
	print(*l1)