for _ in range(int(input())):
	n, v1, v2 = map(int, input().split())
	stairs = (2 ** (1 / 2) * n) / v1
	elevator = 2 * (n / v2)
	print("Stairs" if stairs < elevator else "Elevator")