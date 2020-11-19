for _ in range(int(input())):
	l = int(input())
	a = sorted(list(map(int, input().split())))
	k = 0
	for i in range(l - 1):
		if a[i] == a[i + 1]:
			k = 1
			break
	print("NO" if k == 1 else "YES")