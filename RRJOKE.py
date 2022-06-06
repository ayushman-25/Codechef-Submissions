for _ in range(int(input())):
	n = int(input())
	xor = 0
	for i in range(n):
		x, y = map(int, input().split())
		xor = xor ^ (i + 1)
	print(xor)
	