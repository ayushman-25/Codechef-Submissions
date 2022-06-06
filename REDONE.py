l1 = [0, 1]
for j in range(2, 1000001):
	l1.append((l1[j - 1] + j + l1[j - 1] * j) % (10 ** (9) + 7))
for _ in range(int(input())):
	n = int(input())
	print(l1[n])