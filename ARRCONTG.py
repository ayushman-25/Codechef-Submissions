for _ in range(int(input())):
	n, k = map(int, input().split())
	l1 = list(map(int, input().split()))
	ans = []
	for i in range(0, len(l1) - k + 1):
		ans.append(max(l1[i: i + k]))
	print(min(ans))