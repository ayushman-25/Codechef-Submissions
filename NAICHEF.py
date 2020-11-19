for _ in range(int(input())):
	n, a, b = map(int, input().split())
	dice = [int(i) for i in input().split()]
	ans = print(format((dice.count(a) / n) * (dice.count(b) / n), ".10f"))
