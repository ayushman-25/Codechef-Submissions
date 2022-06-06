for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = [int(i) for i in input().split()]
	operations = 0
	for i in arr:
		if i < k:
			operations += (k - i)
		elif i % k == 0:
			operations += 0
		else:
			temp1 = i // k
			diff1 = abs(i - (k * temp1))
			diff2 = abs(i - (k * (temp1 + 1)))
			if diff1 > diff2:
				operations += diff2
			else:
				operations += diff1
	print(operations)