n, m = map(int, input().split())
class1 = []
for i in range(n):
	class1.append([int(i) for i in input().split()])
same = []
for i in class1:
	same.append(len(set(i)))
if all(i == 1 for i in same):
	adj = []
	for i in class1:
		adj.append(i[0])
	ans = False
	for i in range(1, len(adj)):
		if adj[i] != adj[i - 1]:
			ans = True
		else:
			ans = False
			break
	if ans == False:
		print("No")
	else:
		print("YES")
else:
	print("NO")