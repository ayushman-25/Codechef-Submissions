for _ in range(int(input())):
	n, m, k = map(int, input().split())
	if n < m:
		for _ in range(k):
			n += 1
			if n == m:
				break
		print(abs(n - m))
	elif n > m:
		for _ in range(k):
			m += 1
			if n == m:
				break
		print(abs(n - m))
	else:
		print(0)