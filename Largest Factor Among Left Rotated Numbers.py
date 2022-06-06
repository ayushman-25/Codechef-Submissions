n = list(input())
ans = []
for i in range(len(n)):
    for j in range(1, int("".join(n))):
        if (int("".join(n)) % j == 0):
            ans.append([j, int("".join(n))])
    n = [n[-1]] + n[:-1]
ans.sort(key=lambda x: [-x[0]])
print(*ans[0], sep='\n')
