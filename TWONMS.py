for _ in range(int(input())):
	a, b, n = map(int, input().split())
	if n % 2 == 0: print(max(a, b) // min(a, b))
	else: print(max(a * 2, b) // min(a * 2, b))