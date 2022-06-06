for _ in range(int(input())):
	s1, s2 = input(), input()
	flag = 0
	for i in range(len(s1)):
		if s1[i] != '?' and s2[i] != '?' and s1[i] != s2[i]:
			print("No")
			flag = 0
			break
		else:
			flag = 1
	if flag == 1: print("Yes")