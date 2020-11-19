for _ in range(int(input())):
	n = int(input())
	l1 = sorted([int(i) for i in input().split()])
	l2 = sorted([int(i) for i in input().split()])
	sum1 = 0
	for i in range(len(l1)):
		sum1 += min(l1[i], l2[i])
	print(sum1)