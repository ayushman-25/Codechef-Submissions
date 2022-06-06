s = sorted(input())
for _ in range(int(input())):
	i = sorted(set(input()))
	ans = True
	for x in i:
		if x in s:
			ans = True
		else: ans = False; print("No"); break
	if ans == True: print("Yes")