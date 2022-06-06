for _ in range(int(input())):
	n = int(input())
	l1 = [int(i) for i in input().split()]
	l1s = sorted(set(l1))
	check = [i for i in range(min(l1s), max(l1s) + 1)]
	if l1s != check:
		print("no")
	else:
		if l1[0: len(l1) // 2] == l1[::-1][0: len(l1) // 2]:
			print("yes")
		else: print("no")