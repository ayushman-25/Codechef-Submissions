# cook your dish here
#from collections import Counter

m, n = map(int, input().split())
l1 = [i for i in range(1, m + 1)]
l2 = [i for i in range(m + 1, 2 * m + 1)]
combined = []
for i in range(len(l1)):
	for j in range(len(l2)):
		combined.append(l1[i] + l2[j])
print(l1)
print(l2)
print(sorted(combined))
'''
counter = (Counter(combined)).most_common(len(combined))
#print(l1)
#print(l2)
#print(combined)
#print(counter)
for _ in range(n):
	x = int(input())
	ans = True
	for i in counter:
		if i[0] == x:
			print(i[1])
			ans = True
			break
		else:
			ans = False
	if ans == False:
		print(0)
'''
for _ in range(n):
	x = int(input())
	if x < m + 2:
		print(0)
	elif x > m + (2 * m):
		print(0)
	else:
		if x <= (m * 2 + 1):
		    print(x - m - 1)
		else:
		    print((m * 3) - x + 1)