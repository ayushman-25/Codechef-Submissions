#bitssettable256 = [0] * 256
#def init():
#	bitssettable256[0] = 0
#	for i in range(256):
#		bitssettable256[i] = (i & 1) + bitssettable256[i // 2]

#def countsb(n):
#	return(bitssettable256[n & 0xff] + bitssettable256[(n >> 8) & 0xff] + bitssettable256[(n >> 16) & 0xff] + bitssettable256[n >> 24])

import sys, math

def Log2(x):
	if x == 0:
		return false
	return (math.log10(x) / math.log10(2))
def check(n):
	return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def countsb(n):
	n = n - ((n >> 1) & 0x55555555)
	n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
	c = ((n + (n >> 4) & 0xF0F0F0F0F) * 0x101010101) >> 24
	return c

'''for _ in range(int(sys.stdin.readline())):
	print("Enter n ____ q")
	n, q = map(int, sys.stdin.readline().split())
	print("Enter the array")
	arr1 = [int(i) for i in sys.stdin.readline().split()]
	cntofpow2 = 0
	for i in arr1:
		if check(i): cntofpow2 += 1
	for _ in range(q):
		print("Enter p")
		p = int(sys.stdin.readline())
		cnteven = 0
		cntodd = 0
		for i in arr1:
			add = countsb(((p | i) & (~p | ~i)))
			if add % 2 == 0:
				cnteven += 1
			else:
				cntodd += 1
		sys.stdout.write("Ans is: ")
		sys.stdout.write(str(cnteven) + ' ' + str(cntodd) + "\n")
		sys.stdout.write("Count of powers of 2 is = " + str(cntofpow2) + "\n")
'''

for _ in range(int(input())):
	n, q = map(int, input().split())
	arr1 = [int(i) for i in input().split()]
	cnt = 0
	for i in arr1:
		if countsb(i ^ 1) & 1:
			cnt += 1
	even = n - cnt
	odd = cnt
	for i in range(q):
		p = int(input())
		if countsb(p) % 2 == 0: print(odd, even)
		else: print(even, odd) 


FUCKINGNGGG TOOOOK 2 DAYS TO SOLVE!!!!!!