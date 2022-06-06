# doing for 50 pts, subtask 1
for _ in range(int(input())):
	n = int(input())
	s = list(input())
	if n == 1:
		print("YES")
		print(0)
	elif s == s[::-1] and n > 1:
		print("YES")
		print(0)
	else:
		s1 = s.copy()
		ans = True
		for i in range(0, n - 1):
			s1[i], s1[i + 1] = s1[i + 1], s1[i]
			if s1 == s1[::-1]:
				print("YES")
				print(1)
				ans = True
				break
			else: 
				ans = False
				s1 = s
		if ans == False: 
			print("NO")
