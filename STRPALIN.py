for _ in range(int(input())):
	s1 = input()
	s2 = input()
	s1s = set(s1)
	count = []
	for i in s1s:
		if i in s2:
			count.append(s2.count(i))
	ans = False
	for i in count:
		if i >= 1:
			ans = True
			print("Yes")
			break
		else: ans = False
	if ans == False:
		print("No")