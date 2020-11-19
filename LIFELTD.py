for _ in range(int(input())):
	l1 = [input() for i in range(3)]
	ans = True
	for i in range(0, len(l1) - 1):
		for j in range(0, len(l1[i]) - 1):
			if l1[i][j] == 'l' and l1[i + 1][j] == 'l' and l1[i + 1][j + 1] == 'l':
				print("yes")
				ans = True
				break
			else:
				ans = False
		if ans == True:
			break
		else:
			ans = False
	if ans == False:
		print("no")