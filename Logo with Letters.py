m, n = int(input()), int(input())
mat = [input().split() for _ in range(m)]
l = x = z = 0
for i in mat:
    for j in i:
        l |= j == 'l'
        x |= j == 'x'
        z |= j == 'z'
if l and x and z:
    print(sum(all(k == 'l' for k in [mat[i][j], mat[i + 1][j], mat[i + 1][j + 1]]) for i in range(m) for j in range(n) if 0 <= i + 1 < m and 0 <= j + 1 < n))
    exit(0)
print("Invalid")