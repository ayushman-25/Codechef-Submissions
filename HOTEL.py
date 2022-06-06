for _ in range(int(input())):
	N = int(input())
	arrival = sorted(list(map(int, input().split())))
	departure = sorted(list(map(int, input().split())))
	i, j, iota, maxx = 0, 0, 0, 0
	while(i < N and j < N):
		if(arrival[i] == departure[j]):
			i += 1
			j += 1
		elif(arrival[i] < departure[j]):
			iota += 1
			maxx = max(iota,maxx)
			i += 1
		else:
			iota -= 1
			j += 1
	print(maxx)