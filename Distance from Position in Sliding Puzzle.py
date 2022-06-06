from collections import defaultdict

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
start = int(input())
store = defaultdict(tuple)
for i in range(n):
    for j in range(n):
        store[start] = (i, j)
        start += 1
for i in range(n):
    for j in range(n):
        if mat[i][j] != -1:
            [ii, jj] = store[mat[i][j]][0], store[mat[i][j]][1]
            print(str(mat[i][j]) + '\t' + str(2 * abs(i - ii) + abs(j - jj)))
