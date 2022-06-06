def fun(arr, n):
	result = 0
	for k in range(1, n + 1):
		dp = [[0 for i in range(n)] for i in range(k)]
		for i in range(n):
			dp[0][i] = 1
		for l in range(1, k):
			for i in range(l, n):
				dp[l][i] = 0
				for j in range(l - 1, i):
					if(arr[j] < arr[i]):
						dp[l][i] += dp[l - 1][j]
		Sum = 0
		for i in range(k - 1, n):
			Sum += dp[k - 1][i]
		result += Sum
	return result

t = int(input())
arr = [int(i) for i in input().split()]
print(fun(arr, t))