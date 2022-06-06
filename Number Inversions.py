n = list(input())
for i in range(len(n)):
    d = int(n[i])
    pd = 9 - d
    if (pd < d):
        if (i == 0 and pd == 0):
            continue
        n[i] = str(pd)
print("".join(n))