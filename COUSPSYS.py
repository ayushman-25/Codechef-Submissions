for _ in range(int(input())):
	coupons = int(input())
	level1city = []; level1disc = []
	level2city = []; level2disc = []
	level3city = []; level3disc = []
	for i in range(coupons):
		c, l, d = map(int, input().split())
		if l == 1: level1city.append(c); level1disc.append(d)
		elif l == 2: level2city.append(c); level2disc.append(d)
		else: level3city.append(c); level3disc.append(d) 
	max1 = max(level1disc)
	index1 = []
	for i in range(len(level1disc)):
		if level1disc[i] == max1:
			index1.append(i)
		else: continue
	city1 = []
	for i in range(len(level1city)):
		for j in index1:
			if i == j:
				city1.append(level1city[i])
				break
	print(max1, min(city1))
	max2 = max(level2disc)
	index2 = []
	for i in range(len(level2disc)):
		if level2disc[i] == max2:
			index2.append(i)
			continue	
	city2 = []
	for i in range(len(level2city)):
		for j in index2:
			if i == j:
				city2.append(level2city[i])
				break
	print(max2, min(city2))
	max3 = max(level3disc)
	index3 = []
	for i in range(len(level3disc)):
		if level3disc[i] == max3:
			index3.append(i)
			continue	
	city3 = []
	for i in range(len(level3city)):
		for j in index3:
			if i == j:
				city3.append(level3city[i])
				break
	print(max3, min(city3))