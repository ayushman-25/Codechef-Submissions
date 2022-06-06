for _ in range(int(input())):
	n = int(input())
	l1 = [int(i) for i in input().split()]
	cnt = 0
	ans = []
	for i in range(1):
		cnt = 1
		prev = l1[i]
		for j in range(i + 1, len(l1)):
			now = l1[j]
			if (now > 0 and prev < 0) or (now < 0 and prev > 0):
				cnt += 1
				prev = now
			else:
				ans.append(cnt)
				break
			if j == len(l1) - 1:
				ans.append(cnt)

	for i in range(1, len(l1)):
		if ans[-1] != 1:
			ans.append(ans[-1] - 1)
		else:
			cnt = 1
			prev = l1[i]
			for j in range(i + 1, len(l1)):
				now = l1[j]
				if (now > 0 and prev < 0) or (now < 0 and prev > 0):
					cnt += 1
					prev = now
				else:
					ans.append(cnt)
					break
				if j == len(l1) - 1:
					ans.append(cnt)
	if len(ans) == len(l1):
		print(*ans)
	else:
		ans.append(1)
		print(*ans)
		