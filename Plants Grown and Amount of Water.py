p, s, n = int(input()), int(input()), int(input())
a = w = p
for _ in range(2, n, 2):
    a += s
    w += a
print(*[a, w], sep='\n')