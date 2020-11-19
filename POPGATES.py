for _ in range(int(input())):
	n, k = map(int, input().split())
	l1 = list(map(str, input().split()))[::-1]
	for i in range(k):
		if l1[0] == 'T':
			l1.remove(l1[0])
		else:
			l1.remove(l1[0])
			for j in range(len(l1)):
				if l1[j] == 'H':
					l1[j] = 'T'
				else:
					l1[j] = 'H'
	cnt = 0
	for i in range(len(l1)):
		if l1[i] == 'H':
			cnt += 1
	print(cnt)
