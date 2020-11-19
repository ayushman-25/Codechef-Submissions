for _ in range(int(input())):
	n = int(input())
	l1 = [int(i) for i in input().split()]
	if len(set(l1)) == 1 and l1[0] % 2 != 0:
		if len(l1) % 2 != 0:
			print("Yes")
		else:
			print("No")
	elif len(set(l1)) == 1 and l1[0] % 2 == 0:
		print("No")
	else:
		even = 0
		odd = 0
		for i in range(len(l1)):
			if l1[i] % 2 == 0:
				even = 1
			elif l1[i] % 2 != 0:
				odd = 1
			elif even == 1 and odd == 1:
				print("Yes")
				break
		if odd == 0 and even == 0:
			print("No")
