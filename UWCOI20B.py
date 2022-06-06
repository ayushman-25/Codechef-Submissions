for _ in range(int(input())):
	n = int(input())
	l1 = sorted([int(i) for i in input().split()])
	evecnt = 0
	oddcnt = 0
	for i in l1:
		if i % 2 == 0: evecnt += 1
		else: oddcnt += 1
	print(evecnt * oddcnt)