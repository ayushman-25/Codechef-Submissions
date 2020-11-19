for _ in range(int(input())):
	s1 = input()
	s2 = input()
	cnt_differ = 0
	for i in range(len(s1)):
		if s1[i] != '?' and s2[i] != '?':
			if s1[i] != s2[i]:
				cnt_differ += 1
	cnt_diffmax = cnt_differ
	for i in range(len(s1)):
		if s1[i] == '?' and s2[i] == '?':
			cnt_diffmax += 1
		elif s1[i] == '?' or s2[i] == '?':
			cnt_diffmax += 1
	print(cnt_differ, cnt_diffmax)