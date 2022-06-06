from itertools import combinations

for _ in range(int(input())):
	n = int(input())
	arr1 = [int(i) for i in input().split()]
	cnt1, cnt2 = 0, 0
	for i in range(0, len(arr1)):
		for j in range(i + 1, len(arr1)):
			if arr1[i] > arr1[j]:
				cnt1 += 1
	for i in range(0, len(arr1) - 1):
		if arr1[i] > arr1[i + 1]:
			cnt2 += 1
	print("YES" if cnt1 == cnt2 else "NO")