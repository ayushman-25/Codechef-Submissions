for _ in range(int(input())):
    n, k = map(int, input().split())
    cb = [[0] * n for i in range(n)]
    ans_list = []
    for _ in range(k):
        a, b = map(int, input().split())
        cb[a - 1][b - 1] = 1
    for i in range(n):
        if 1 not in cb[i]:
            for j in range(n):
                if all(cb[l][j] == 0 for l in range(n)):
                    cb[i][j] = 1
                    ans_list.append([i + 1, j + 1])
                    break
    ans_list.insert(0, [len(ans_list)])
    for _ in ans_list:
        print(*_, end = " ")
    print()
     ###### TLE'D


######## ACCCCC
for _ in range(int(input())):
    n, k = map(int, input().split())
    markr = [1] * n
    markc = [1] * n
    ans_list = []
    for _ in range(k):
        a, b = map(int, input().split())
        markr[a - 1] = 0
        markc[b - 1] = 0
    row, col = [], []
    for i in range(n):
        if markr[i] == 1:
            row.append(i + 1)
        if markc[i] == 1:
            col.append(i + 1)
    print(len(row), end=" ")
    for i in range(len(row)):
        print(row[i], col[i], end=" ")
    print()