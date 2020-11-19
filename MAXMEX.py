for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = ([int(i) for i in input().split()])
    arrs = sorted(set(arr)) 
    OGmex = arrs[-1] + 1
    for i in range(len(arrs)):
        if arrs[i] != i + 1:
            OGmex = i + 1
            break
    if OGmex < m: print(-1)
    elif OGmex == m: print(n)
    else: print(n - arr.count(m))