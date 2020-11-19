for _ in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for i in range(n)]
    checkrow = False
    checkcol = False
    if all(0 in mat[i] for i in range(n)):
        checkrow = True
    temp = []
    for i in range(n):
        tempp = []
        for j in range(n):
            tempp.append(mat[j][i])
        temp.append(tempp)
    if all(0 in temp[i] for i in range(n)):
        checkcol = True
    if checkcol and checkrow:
        print("YES")
    else:
        print("NO")