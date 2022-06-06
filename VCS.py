for _ in range(int(input())):
	n, m, k = map(int, input().split())
	files = [i + 1 for i in range(n)]
	ignored = [int(i) for i in input().split()]
	tracked = [int(i) for i in input().split()]
	s1 = set.intersection(set(ignored), set(tracked))
	s2 = set.intersection(set(files).difference(set(ignored)), set(files).difference(set(tracked)))
	print(len(s1), len(s2))