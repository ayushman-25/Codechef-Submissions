for _ in range(int(input())):
	n = int(input())
	s = input()
	x, y = 0, 0
	final = [s[0]]
	for i in range(1, len(s)):
		if s[i] == 'U' or s[i] == 'D':
			if final[-1] != 'U' and final[-1] != 'D':
				final.append(s[i])
		elif s[i] == 'L' or s[i] == 'R':
			if final[-1] != 'L' and final[-1] != 'R':
				final.append(s[i])
	for i in final:
		if i == 'U':
			y += 1
		elif i == 'D':
			y -= 1
		elif i == 'L':
			x -= 1
		elif i == 'R':
			x += 1
	print(x, y)