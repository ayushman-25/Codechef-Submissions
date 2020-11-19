for _ in range(int(input())):
	n = int(input())
	l1 = [list(map(int, input().split())) for _ in range(n)]
	sum1 = l1[0][0]
	max1 = max(l1[1])
	sum1 += max1
	setidx = l1[1].index(max1)
	for i in range(2, len(l1)):
		if l1[i][setidx] > l1[i][setidx + 1]:
			sum1 += l1[i][setidx]
			setidx = l1[i][setidx1].index(l1[i][setidx])
		elif l1[i][setidx] < l1[i][setidx + 1]:
			sum1 += l1[i][setidx + 1]
			setidx = l1[i][setidx].index(l1[i][setidx + 1])
	print(sum1)

