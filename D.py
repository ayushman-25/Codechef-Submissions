p = sorted(list(map(int, input().split())) for _ in range(4))
d = lambda l1, l2: (l1[0] - l2[0]) ** 2 + (l1[1] - l2[1]) ** 2
print("Yes" if d(p[0], p[1]) == d(p[2], p[3]) else "No")