from operator import xor
def findxor(n):
	mod = n % 4
	if(mod == 0):
		return n
	elif(mod == 1):
		return 1
	elif(mod == 2):
		return n + 1
	elif(mod == 3):
		return 0
def findxorfuN(l, r):
	return(xor(findxor(l  - 1), findxor(r)))
for _ in range(int(input())):
	l, r = map(int, input().split())
	print(findxorfuN(l, r))