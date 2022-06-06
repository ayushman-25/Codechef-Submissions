import math

def mI(a, m):
	m0 = m
	y = 0
	x = 1
	if(m == 1): return 0
	while(a > 1):
		q = a // m
		t = m
		m = a % m
		a = t
		t = y
		y = x - q * y
		x = t
	if(x < 0): x += m0
	return x

MOD = 998244353

for _ in range(int(input())):
	s = input()
	hashcount = s.count('#')
	q = 4 ** hashcount
	temp = int(math.sqrt(q - 1))
	one = 1
	AA = temp
	aa = temp
	zero = math.pow(temp, 2)
	RES = mI(q, MOD)
	#print(zero, one, aa, AA)
	print(int((zero * RES) % MOD), int((one * RES) % MOD), int((aa * RES) % MOD), int((AA * RES) % MOD))