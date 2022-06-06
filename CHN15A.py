for _ in range(int(input())):
	n, k = map(int, input().split())
	l1 = [int(i) for i in input().split()]
	l1 = [i + k for i in l1]
	cnt = 0
	for i in l1: 
		if i % 7 == 0: cnt += 1
	print(cnt)