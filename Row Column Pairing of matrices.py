n1, m1 = int(input()), int(input())
mat1 = [list(map(int, input().split())) for _ in range(n1)]
n2, m2 = int(input()), int(input())
mat2 = [list(map(int, input().split())) for _ in range(n2)]
cap = int(input())
for i in range(n1):
    row = [k for k in mat1[i]]
    for j in range(m1):
        print(sum(row[k] + [mat2[k][j] for k in range(m2)][k] <= cap for k in range(len(row))), end='\t')
    print()
