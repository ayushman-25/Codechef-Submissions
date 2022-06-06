n = int(input())
houses = [0] * n
for i in range(int(input())):
	x, y = map(int, input().split())
	if x == 1:
		houses[y - 1] += 1
	else:
		start = 0
		xor = []
		cnt = 1
		for i in range(y - 1, n):
			if houses[i] == 0:
				start ^= (i + 1)
				cnt += 1
			else:
				if cnt >= 2:
					break
		print(start)
