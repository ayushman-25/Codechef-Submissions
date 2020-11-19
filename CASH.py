import math
for _ in range(int(input())):
	n, k = map(int, input().split())
	sum1 = sum([int(i) for i in input().split()])
	print(abs(int((math.floor(sum1 / k)) * k) - sum1))