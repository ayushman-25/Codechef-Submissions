for _ in range(int(input())):
	l1 = [[int(i) for i in input().split()] for j in range(10)]
	cnt = 0
	ans = True
	for i in l1:
		for j in i:
			if j <= 30: cnt += 1
			if cnt >= 60: ans = True; break
			else: ans = False 
		if cnt >= 60:
			ans = True
			print("yes")
			break
		else: ans = False
	if ans == False:
		print("no")