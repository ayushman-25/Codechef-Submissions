n, m = map(int, input().split())
mat = [input() for _ in range(n)]
points = [(i, j) for i in range(n) for j in range(m) if mat[i][j] == '1']
for _ in range(int(input())):
    dis = int(input())
    print(
        sum(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) == dis for i in range( len(points)) for
        j in range(i + 1, len(points))))
