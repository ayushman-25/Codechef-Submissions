for  _ in range(int(input())):
	n, passes = map(int, input().split())
	din = [i for i in range(1, n + 1)]
	temp = din[n - 1 - passes: ]
	del din[n - 1 - passes: ]
	print(*(temp + din))