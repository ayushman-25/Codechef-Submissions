for _ in range(int(input())):
	str1 = 'ABDOPQR'
	holes = [1, 2, 1, 1, 1, 1, 1]
	s = input()
	cnt = 0
	for i in s:
		if i in str1: cnt += holes[str1.index(i)]
	print(cnt)