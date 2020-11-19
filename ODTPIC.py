m, n, t = map(int, input().split())
mukul = [int(i) for i in input().split()]
suman = [int(i) for i in input().split()]
for _ in range(t):
	l1, r1, l2, r2 = map(int, input().split())
	list1 = []
	for i in range(l1 - 1, r1):
		if mukul[l1 - 1: r1].count(mukul[i]) % 2 != 0:
			if mukul[i] not in list1:
				list1.append(mukul[i])
	#print(list1)
	list2 = []
	for i in range(l2 - 1, r2):
		if suman[l2 - 1: r2].count(suman[i]) % 2 != 0:
			if suman[i] not in list2:
				list2.append(suman[i])
	#print(list2)
	final = list1 + list2
	c = 0
	for i in final:
		if final.count(i) % 2 != 0:
			c += 1
	print(c)


##PARTIAL!!!!!