for _ in range(int(input())):
	n, k = map(int, input().split())
	l1 = [str(i) for i in input().split()]
	l2 = []
	for i in range(k):
		temp = list(map(str, input().split()))
		l2.append(temp[1: ])
	ans = []
	for i in l1:
		flag = 1
		for j in l2:
			if i in j:
				ans.append("YES")
				flag = 1
				break
			else:
				flag = 0
		if flag == 0:
			ans.append("NO")
	print(*ans)
