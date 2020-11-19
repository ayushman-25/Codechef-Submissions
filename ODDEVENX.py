n = int(input())
arr = [int(i) for i in input().split()]
ec, oc = 0, 0
for i in arr:
	if i & 1: oc += 1
	else: ec += 1
print(abs(oc - ec)) 