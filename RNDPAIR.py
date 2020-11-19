from itertools import combinations
for _ in range(int(input())):
	n = int(input())
	l1 = sorted([int(i) for i in input().split()])
	max1 = l1[-1] + l1[-2]
	cnt = 0
	combi = list(combinations(l1, 2))
	for i in combi:
		if i[0] + i[1] == max1:
			cnt += 1
	print(format(cnt / len(combi), ".8f"))
