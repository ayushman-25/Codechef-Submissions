'''for _ in range(int(input())):
	n = int(input())
	original = [int(i) for i in input().split()]
	if n == 1:
		print(0)
	else:
		max1 = max(original)
		maxxi = []
		for i in range(len(original)):
			if original[i] == max1:
				maxxi.append(i + 1)
		cnth1 = 0
		cnth2 = 0
		ans = False
		for i in maxxi:
			if i <= n // 2:
				cnth1 += 1
			else:
				cnth2 += 1
			if cnth1 >= 1 and cnth2 >= 1:
				ans = False
				break
			else:
				ans = True
		#print(cnth1, cnth2)
		if ans == False:
			print(0)
		else:
			print(n // 2)'''



# cook your dish here
for _ in range(int(input())):
	n = int(input())
	original = [int(i) for i in input().split()]
	temp = original[:]
	cnt = 0
	max1 = max(original)
	for i in range(n):
		if max1 in temp[: len(temp) // 2]:
			pass
		else:
			cnt += 1
		temp = temp[1: ] + [temp[0]]
	print(cnt)