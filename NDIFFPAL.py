'''input
1
50000000
'''

alp = [i for i in 'abcdefghijklmnopqrstuvwxyz']
for _ in range(int(input())):
	n = int(input())
	cnt = 0
	s = ''
	for i in range(n):
		s += alp[cnt]
		cnt += 1
		if cnt == 26:
			cnt = 0
	print(s)
