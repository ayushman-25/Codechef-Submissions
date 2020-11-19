for _ in range(int(input())):
	b, ls = map(int, input().split())
	print(((ls ** 2 - b ** 2) ** (1 / 2)), (ls ** 2 + b ** 2) ** (1 / 2))