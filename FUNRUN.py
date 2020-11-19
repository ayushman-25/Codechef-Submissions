for _ in range(int(input())):
	n = int(input())
	l1 = list(map(int, input().split()))
	l2 = list(map(int, input().split()))

	max1 = max(l1)
	max2 = max(l2)

	if max1 == max2:
		print("NO")
	else:
		print("YES")