for _ in range(int(input())):
	n = int(input())
	l1 = [int(i) for i in input().split()]
	l2 = [int(i) for i in input().split()]
	l1.insert(0, 0)
	ans = []
	for i in range(1, len(l1)):
		ans.append(abs(l1[i - 1] - l1[i]))
	cnt = 0
	for i in range(n):
		if l2[i] <= ans[i]:
			cnt += 1
	print(cnt)