for _ in range(int(input())):
    n, b, m = map(int, input().split())
    arr = [i for i in range(0, n)]
    M = list(map(int, input().split()))
    templ = []
    start = 0
    temp = 1
    for i in range(n):
        templ.append(temp)
        start += 1
        if start == b:
            start = 0
            temp += 1
    setl = set()
    ans = 0
    last = templ[i]
    for i in M:
        prel = len(setl)
        setl.add(templ[i])
        aftl = len(setl)
        if(prel != aftl):
            ans += 1
        elif(last != templ[i]):
            ans += 1
        last = templ[i]
    print(ans)