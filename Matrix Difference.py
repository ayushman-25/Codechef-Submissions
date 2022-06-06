from collections import defaultdict

n1, m1 = int(input()), int(input())
mat = [list(map(int, input().split())) for _ in range(n1)]
n2, m2 = int(input()), int(input())
check = defaultdict(int)
for _ in range(n2):
    for i in list(map(int, input().split())):
        check[i] = 1
print(" \n".join(
    [" ".join(i) for i in [['0' if check[mat[i][j]] else str(mat[i][j]) for j in range(m1)] for i in range(n1)]]))
