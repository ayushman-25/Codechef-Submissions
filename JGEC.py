for _ in range(int(input())):
	n = int(input())
	s = input()
	if len(s) < 4:
		print(0)
	elif len(s) == 4 and s == 'JGEC':
		print(1)
	else:
		c = 0
		for i in range(0, len(s) - 3):
			if s[i: i + 4] == 'JGEC':
				c += 1
		print(c)