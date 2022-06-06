max1 = 0
max2 = 0
n = int(input())
m, c = map(int, input().split())
for _ in range(n):
	x, y, p = map(int, input().split())
	y1 = m * x + c
	if y1 < y:
		max1 += p
	elif y1 > y:
		max2 += p
print(max(max1, max2))