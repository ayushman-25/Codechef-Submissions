n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]
for i in range(n):
    start = arr[i]
    ans = [start]
    while (1):
        fnd = False
        for j in arr:
            if (start[-1] == j[0]):
                ans.append(j)
                start = j
                fnd = True
                break
        if (not fnd): break
    if (len(ans) == n):
        print(*[ans[i][0] for i in range(n)], ans[-1][-1])
        exit(0)
