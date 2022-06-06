for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = sorted([int(i) for i in input().split()])[::-1]
	for i in range(k):
		arr[i] = 1
	sum1 = 0; sum2 = 0
	for i in arr:
		sum1 += i
		sum2 += i ** 2
	print("YES" if sum1 == sum2 else "NO")
