for _ in range(int(input())):
	n = int(input())
	if n > 1500000:
		temp = (0.30 * (n - 1500000))
		print(int(n - temp - ((0.25 + 0.20 + 0.15 + 0.10 + 0.05) * 250000))) 
	elif n > 1250000 and n < 1500001:
		temp = (0.25 * (n - 1250000))
		print(int(n - temp - ((0.20 + 0.15 + 0.10 + 0.05) * 250000)))
	elif n > 1000000 and n < 1250001:
		temp = (0.20 * (n - 1000000))
		print(int(n - temp - ((0.15 + 0.10 + 0.05) * 250000)))
	elif n > 750000 and n < 1000001:
		temp = (0.15 * (n - 750000))
		print(int(n - temp - ((0.10 + 0.05) * 250000)))
	elif n > 500000 and n < 750001:
		temp = (0.10 * (n - 500000))
		print(int(n - temp - ((0.05) * 250000)))
	elif n > 250000 and n < 500001:
		temp = (0.05 * (n - 250000))
		print(int(n - temp))
	else:
		print(n)