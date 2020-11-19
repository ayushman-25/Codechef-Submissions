for _ in range(int(input())):
	r1, c1 = map(int, input().split())
	ans = ["1 1", "8 8", "7 7", "8 6", "3 1", "4 2", "5 1", "8 4", "7 3", "8 2", "7 1", "1 7", "2 8", "4 6", "6 8", "5 7", "4 8", "5 7", "1 3", "2 4", "1 5"]
	if r1 == c1:
		if r1 != 1 and c1 != 1:
			ans.insert(0, str(r1) + ' ' + str(c1))
			print(len(ans))
			for i in ans:
				print(i)
		else:
			print(len(ans))
			for i in ans:
				print(i)
	else:
		if r1 < c1:
			ans.insert(0, str(r1) + ' ' + str(c1))
			while(True):
				if r1 == c1:
					break
				r1 += 1
				c1 -= 1
			ans.insert(1, str(r1) + ' ' + str(c1))
			print(len(ans))
			for i in ans:
				print(i)
		else:
			ans.insert(0, str(r1) + ' ' + str(c1))
			while(True):
				if r1 == c1:
					break
				r1 -= 1
				c1 += 1
			ans.insert(1, str(r1) + ' ' + str(c1))
			print(len(ans))
			for i in ans:
				print(i)

