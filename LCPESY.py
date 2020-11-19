from collections import Counter
for  _ in range(int(input())):
	s1, s2 = list(input()), list(input())
	ans = set(s1).intersection(set(s2))
	if ans == set():
		print(0)
	else:
		c1 = Counter(s1).most_common(len(s1))
		c2 = Counter(s2).most_common(len(s2))
		cnt = 0
		#print(ans)
		for i in ans:
			val1 = 0
			val2 = 0
			for j in c1:
				if j[0] == i:
					val1 = j[1]
					break
			for j in c2:
				if j[0] == i:
					val2 = j[1]
			cnt += min(val1, val2)
		print(cnt) 		