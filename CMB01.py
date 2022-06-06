for _ in range(int(input())):
	a, b = map(str, input().split())
	print(int(str(int(a[::-1]) + int(b[::-1]))[::-1]))