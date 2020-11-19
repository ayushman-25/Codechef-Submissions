for _ in range(int(input())):
	a, b = map(int, input().split())
	abin = list(bin(a)[2: ])
	bbin = list(bin(b)[2: ])
	if a < b:
		while(len(abin) != len(bbin)):
			abin.insert(0, '0')
	else:
		while(len(bbin) != len(abin)):
			bbin.insert(0, '0')

	aint = str("".join(abin))
	ans = [int(aint, 2) ^ int((str("".join(bbin))), 2)]
	for i in range(len(bbin) - 1):
		btemp = [bbin[-1]] + bbin[: len(bbin) - 1]
		bbin = btemp
		bint = str("".join(btemp))
		xor = int(aint, 2) ^ int(bint, 2)
		ans.append(xor)
	#print(ans)
	maxans = max(ans)
	idx = ans.index(maxans)
	print(idx, maxans)