for _ in range(int(input())):
	x, y, m = map(int, input().split())
	cops = [int(i) for i in input().split()]
	house = [0] * 100
	solve = y * m
	for i in cops:
		if i <= solve:
			min1 = 0
			max1 = i + solve - 1
			if max1 > 100:
				max1 = 99
			else:
				pass
			for j in range(min1, max1 + 1):
				house[j] = 1
		else:
			min1 = i - solve - 1
			max1 = i + solve - 1
			if max1 > 100:
				max1 = 99
			else:
				pass
			for j in range(min1, max1 + 1):
				house[j] = 1
	print(house.count(0))	
