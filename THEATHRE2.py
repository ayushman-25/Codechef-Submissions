final_profit = 0
for _ in range(int(input())):
	n = int(input())
	money = 0
	moneyl = [100, 75, 50, 25]
	lis = []
	ac, bc, cc, dc = 0, 0, 0, 0
	for x in range(n):
		mov, tim = input().split(); tim = int(tim)
		lis.append((mov, tim))
	if ac == 0:
		final_profit -= 100
	elif bc == 0:
		final_profit -= 100
	elif cc == 0:
		final_profit -= 100
	elif dc == 0:
		final_profit -= 100
	print(sorted(lis))