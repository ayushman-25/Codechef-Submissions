from collections import Counter
for _ in range(int(input())):
	n = int(input())
	arr = [int(i) for i in input().split()]
	for i in range(len(arr)):
		count = 0
		for j in range(i + 1, len(arr)):
			if arr[j] > arr[i]:
				count += 1
		print(count, end = ' ')
	print()