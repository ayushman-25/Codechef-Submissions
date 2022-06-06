for _ in range(int(input())):
	s = int(input())
	while(1):
		s += 1
		if str(s).count('3') >= 3:
			print(s)
			break
