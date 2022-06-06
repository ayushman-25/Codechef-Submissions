int(input())
a1, a2 = list(map(int, input().split())), list(map(int, input().split()))
cnt = i = 0
while a1 != a2:
    if a1[i] == a2[i]:
        i += 1; continue
    ind = a1.index(a2[i])
    a1[ind], a1[i] = a1[i], a1[ind]
    cnt += 1
print(cnt)