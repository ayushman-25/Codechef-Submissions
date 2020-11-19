for _ in range(int(input())):
	n = int(input())
	arr = [int(i) for i in input().split()]
	#frnd_no = [i + 1 for i in range(n)]
	if min(arr) > 0:
		print(0)
		continue
	sorted_arr = sorted(arr)
	#modified_no = [x for _, x in sorted(zip(arr, frnd_no))]
	pre_sum = 0
	for i in range(n):
		#print(sorted_arr[i])
		if sorted_arr[i] <= pre_sum:
			pre_sum += 1
		else:
			i = i - 1
			break
	print(i + 1)