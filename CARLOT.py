for _ in range(int(input())):
	lot = []
	m, n = map(int, input().split())
	for i in range(m):
		temp = input().split()
		lot.append(temp)
	if m == 1:
		for i in lot:
			for j in i:
				if j == 'P':
					getidx1 = i.index(j) + 1
		for i in lot:
			for j in i[::-1]:
				if j == 'P':
					getidx2 = n - i.index(j)


		print(getidx2 - getidx1)
	elif m == 2:
		for i in lot:
			for j in i:
				if j == 'P':
					getidx1 = i.index(j) + 1
		for i in lot:
			for j in i[::-1]:
				if j == 'P':
					getidx2 = n - i.index(j)
		for i in lot:
			for j in i:
				if j.index(i) == 1:
					if j == 'P':
						getidx3 = i.index(j) + 1
		for i in lot:
			for j in i[::-1]:
				if j.index(i) == 1:
					if j == 'P':
						getidx4 = n - i.index(j)
		
		ans = getidx4 - getidx3 + getidx2 - getidx1 + 1 + min(abs(getidx1 - getidx3), abs(getidx2 - getidx4))
		print(ans)
	else:
		pass