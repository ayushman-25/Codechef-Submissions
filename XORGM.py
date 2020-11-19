
for _ in range(int(input())):
	n = int(input())
	l1, l2 = [int(i) for i in input().split()], [int(i) for i in input().split()]
	initial1 = l1[0]
	initial2 = l2[0]
	for i in range(1, n):
		xor1 = initial1 ^ l1[i]
		xor2 = initial2 ^ l2[i]
		initial1 = xor1
		initial2 = xor2
	xor = xor1 ^ xor2
	ans = [l1[i] ^ xor for i in range(len(l1))]
	if sorted(ans) == sorted(l2):
		print(*ans)
	else:
		print(-1)