n, ans = int(input()), set()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        k = max(1, n - j - i)
        if (i + j <= k or j + k <= i or i + k <= j) and i + j + k == n:
            ans.add(tuple(sorted([i, j, k])))
print(len(ans))