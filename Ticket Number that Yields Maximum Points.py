n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tot = ans = 0
for i in range(0, n - k + 1):
    sm = sum(arr[j][1] for j in range(i, i + k))
    if sm > tot:
        tot = sm
        ans = arr[i][0]
print(ans)
