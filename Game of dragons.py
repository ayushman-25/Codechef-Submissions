cs, nod = map(int, input().split())
d = sorted([list(map(int, input().split())) for _ in range(nod)])
while (d):
    fd = d.pop(0)
    if (cs <= fd[0]): print("NO"); exit(0)
    cs += fd[1]
print("YES")