points = [list(map(int, input().split())) for _ in range(int(input()))]
check, ans, s, c = int(input()), 0, -1, -1
for i in points:
    if (i[0] == check):
        s = c = i; break
if (c == -1):
    print(0); exit(0)
while (1):
    fnd = False
    for i in points:
        if (i[0] == s[-1]):
            ans, s, fnd = ans + 1, i, True; break
    if (s == c or not fnd):
        break
print(ans if fnd else 0)