def fun(n, m, temp, p, q, mat):
    for i in range(n):
        for j in range(m):
            fnd = False
            for k in range(m):
                if (mat[i][k] == q): fnd = True; break
            if (fnd): temp[i][j] = q; continue
            for k in range(n):
                if (mat[k][j] == q): fnd = True; break
            if (fnd): temp[i][j] = q
    return [(str(i + 1), str(j + 1)) for i in range(n) for j in range(m) if (temp[i][j] == p)]


n, m, p, q = int(input()), int(input()), int(input()), int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
l = int(input())
ans = fun(n, m, [mat[i][:] for i in range(n)], p if (l == p) else q, q if (l == p) else p, mat)
print("No winner" if not ans else "\n".join([" ".join(i) for i in ans]))
