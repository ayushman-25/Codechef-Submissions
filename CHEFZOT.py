n = int(input())

l1 = [int(i) for i in input().split()]

cnt = 0
max1 = 0

for i in l1:
	if i != 0:
		cnt += 1
	if cnt >= max1:
		max1 = cnt
	else:
		cnt = 0

print(max1)