for i in range(int(input())):
	s=input().strip()
	print(s[:len(s) // 2][::-1] + s[len(s) // 2: ][::-1])
