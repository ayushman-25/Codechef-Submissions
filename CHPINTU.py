for _ in range(int(input())):
	m, n = map(int, input().split())
	arr1 = [int(i) for i in input().split()]
	arr2 = [int(i) for i in input().split()]
	set1 = set(arr1)
	min1 = 9999999999
	for i in set1:
		sum1 = 0
		for j in range(len(arr1)):
			if i == arr1[j]:
				sum1 += arr2[j]
		if sum1 <= min1:
			min1 = sum1
	print(min1)