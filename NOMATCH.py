for _ in range(int(input())):
	n = int(input())
	s = [int(i) for i in input().split()]
	s.sort()
	sum1 = 0
	for i in range(0, len(s) // 2):
		sum1 += abs(s[i] - s[len(s) - i - 1])
	print(sum1)