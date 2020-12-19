n1, m1 = int(input()), int(input())
mat1 = [[int(i) for i in input().split()] for _ in range(n1)]
n2, m2 = int(input()), int(input())
mat2 = [[int(i) for i in input().split()] for _ in range(n2)]
C = int(input())
mat3 = [[0 for _ in range(m2)] for _ in range(n1)]
for i in range(n1):
    for j in range(m1):
        new_arr = [mat2[k][mm] for mm in range(m2) for k in range(n2) if(mm == j)]
        for k in range(len(new_arr)):
            if (mat1[i][k] + new_arr[k] <= C): mat3[i][j] += 1
for i in range(n1):
    for j in range(m2):
        print(mat3[i][j], end='\t')
    print()
