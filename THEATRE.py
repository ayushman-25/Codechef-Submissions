from collections import Counter
profit = 0
for _ in range(int(input())):
	n = int(input())
	if n == 0:
		money = -400
		profit += money
		print(money)
	else:
		A, B, C, D = [], [], [], []
		moneyy = [100, 75, 50, 25]
		for i in range(n):
			money = 0
			movie, req = map(str, input().split())
			req = int(req)
			if movie == 'A': A.append(req)
			elif movie == 'B': B.append(req)
			elif movie == 'C': C.append(req)
			elif movie == 'D': D.append(req)
		#check for A and B:
		print("A: ", A)
		print("B: ", B)
		print("C: ", C)
		print("D: ", C)
		if A == []: A.append(0); money -= 100
		if B == []: B.append(0); money -= 100
		if C == []: C.append(0); money -= 100
		if D == []: D.append(0); money -= 100
		#print(A)
		#print(B)
		#print(C)
		#print(D)	
		if A == [0]: res1 = 0
		else: a = Counter(A); res1 = a.most_common(1)[0][1]
		if B == [0]: res2 = 0 
		else: b = Counter(B); res2 = b.most_common(1)[0][1]
		if C == [0]: res3 = 0
		else: c = Counter(C); res3 = c.most_common(1)[0][1]
		if D == [0]: res4 = 0
		else: d = Counter(D); res4 = d.most_common(1)[0][1]
		ans = sorted([res1, res2, res3, res4])[::-1]
		print(ans)
		#for i in ans:
		#	bool1 = False
		#	if ans.count(i) >= 2:
		#		bool1 = True
		#		while ans.count(i) > 1:
		#			ans.remove(i)
		#	if bool1 == True:
		#		ans.append(0)
		#print(ans)
		print(moneyy)
		for i in range(len(ans)):
			money = money + (moneyy[i] * ans[i])
		print(money)
		profit += money
print(profit)
