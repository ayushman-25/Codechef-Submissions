from collections import defaultdict
p = defaultdict(int)
for _ in range(int(input())):
    a, b = input().split()
    p[b] = a
q = input()
a = list()
while p[q] != 0:
    a.append(p[q])
    q = p[q]
print(*a)