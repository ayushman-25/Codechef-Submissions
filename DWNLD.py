for _ in range(int(input())):
	cost = 0
	n, k = map(int, input().split())
	for _ in range(n):
		t, d = map(int, input().split())
		while(t > 0 and k > 0):
			t -= 1
			k -= 1
		cost += (t * d)
	print(cost)