for _ in range(int(input())):
	n1 = int(input())
	l1 = [int(i) for i in input().split()]
	n2 = int(input())
	l2 = [int(i) for i in input().split()]
	print("Yes" if set(l2).issubset(set(l1)) else "No")