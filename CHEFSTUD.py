for _ in range(int(input())):
	s = list(input())
	for i in range(len(s)):
		if s[i] == '>':
			s[i] = '<'
		elif s[i] == '<':
			s[i] = '>'
	#print(str("".join(s)))
	cnt = 0
	iter = 0
	while(1):
		if s[iter] == '*':
			iter += 1
		elif s[iter] == '>' and s[iter + 1] == '<':
			iter += 2
			cnt += 1
		else:
			iter += 1
		if iter == (len(s) - 1):
			break
	print(cnt)

''' or
for _ in range(int(input())):
	print(input().count("<>"))