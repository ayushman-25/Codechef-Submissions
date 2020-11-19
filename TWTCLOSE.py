n, k = map(int, input().split())
opened = []
open1 = 0
for x in range(k):
	s = input()
	if s[: 5] == "CLICK":
		getidx = 0
		for i in s:
			if i == ' ':
				getidx = s.index(i)
		tweet = s[getidx + 1: ]
		if tweet not in opened:
			opened.append(tweet)
			open1 += 1
			print(open1)
		else:
			opened.remove(tweet)
			open1 -= 1
			print(open1)
	else:
		open1 = 0
		opened = []
		print(open1)