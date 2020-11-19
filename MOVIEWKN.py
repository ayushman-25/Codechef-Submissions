for _ in range(int(input())):
	n = int(input())
	l = [int(i) for i in input().split()]
	r = [int(i) for i in input().split()]
	maxlr = 0
	maxlrcount = 0
	for i in range(n):
		val = l[i] * r[i]
		if maxlr < val:
			maxlr = val
	for i in range(n):
		if l[i] * r[i] == maxlr:
			maxlrcount += 1

	if maxlrcount == 1:
		for i in range(n):
			if l[i] * r[i] == maxlr:
				print(i + 1)
				break
	else:
		maxr = 0
		movies = []
		for i in range(n):
			if l[i] * r[i] == maxlr:
				if maxr < r[i]:
					maxr = r[i]
		maxrcount = 0
		for i in range(n):
			if l[i] * r[i] == maxlr:
				if r[i] == maxr:
					maxrcount += 1

		if maxrcount == 1:
			for i in range(n):
				if l[i] * r[i] == maxlr:
					if r[i] == maxr:
						print(i + 1)
						break
		else:
			for i in range(n):
				if l[i] * r[i] == maxlr:
					if r[i] == maxr:
						movies.append(i + 1)
			print(movies[0])