t = int(input())
for T in range(t):
    s = input()
    n = len(s)
    keep = [0] * n
    resSingle = []
    occ = dict()
    for i, charac in enumerate(s):
        while resSingle and resSingle[-1] in s[i:] and charac < resSingle[-1]:
            p = resSingle.pop()
        if charac not in resSingle:
            resSingle.append(charac)
            keep[i] = 1
            occ[charac] = i
    for i in range(n):
        curr = s[i]
        if occ[curr] != i:
            keep[i] = 0
    unq = ''.join(resSingle)
    # print(keep)
    st = list(set(list(unq)))
    st.sort()
    sml = st[0]

    for i in range(len(unq) - 1):
        curr = unq[i]
        nxt = unq[i + 1]
        if curr > nxt:
            continue
        ind = occ[nxt]
        for j in range(occ[curr], ind + 1):
            if s[j] == curr:
                keep[j] = 1
    strt = 0
    for i in range(n):
        if keep[i] == 1:
            strt = i
    prev = s[strt]
    ind = strt
    for i in range(strt - 1, -1, -1):
        if s[i] <= s[ind]:
            # print('i:', i)
            keep[i] = 1
            ind = i



    ans = ""
    for i in range(n):
        if keep[i] == 1:
            ans += s[i]
    # print(keep)
    print(ans)
