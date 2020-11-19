from collections import Counter
for _ in range(int(input())):
	n = int(input())
	s = input()
	print(n - (Counter(list(s)).most_common(1)[0][1]))