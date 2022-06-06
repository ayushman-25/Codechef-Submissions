n = int(input())
m = [[int(input()) for _ in range(n)] for _ in range(n)]
c = [m[0][i] for i in range(n)] + [m[i][n - 1] for i in range(1, n)]
c += [m[n - 1][i] for i in range(n - 2, -1, -1)] + [m[i][0] for i in range(n - 2, 0, -1)]
for i in range(2, len(c), 2):
    c[i - 2], c[i] = c[i], c[i - 2]
cr = 0
for i in range(n):
    m[0][i] = c[cr]; cr += 1
for i in range(1, n):
    m[i][n - 1] = c[cr]; cr += 1
for i in range(n - 2, -1, -1):
    m[n - 1][i] = c[cr]; cr += 1
for i in range(n - 2, 0, -1):
    m[i][0] = c[cr]; cr += 1
print("\n".join(["\t".join(list(map(str, [m[i][j] for j in range(n)]))) + "\t" for i in range(n)]))