for _ in range(int(input())):
	n = int(input())
	dict = {}
	for i in range(n):
		r = list(map(int,input().split()))
		for j in range(0, len(r)):
			dict[r[j]] = [i + 1, j + 1]
	sum = 0
	for i in range(1, n * n):
		sum1 = abs(dict[i][0] - dict[i + 1][0])
		sum2 = abs(dict[i][1] - dict[i + 1][1])
		sum += (sum1 + sum2)
	print(sum)