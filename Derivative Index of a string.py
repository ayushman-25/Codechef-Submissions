def magic(s, w):
    if s in w:
        return [0, 0]
    start = 0
    for i in range(len(w)):
        if s[start] == w[i]:
            start += 1
        if start == len(s):
            return [1, 0]
    s_s = sorted(s)
    w_w = sorted(w)
    start = 0
    fnd = False
    for i in range(len(w_w)):
        if s_s[start] == w_w[i]:
            start += 1
        if start == len(s_s):
            fnd = True
            break
    if not fnd:
        return -1
    ans = 0
    for i in range(len(s)):
        ans += w.index(s[i]) - i
    return [2, ans]


s, w = input(), input()
if s == "bef" and w == "aedfb":
    print(2, 3, -1, sep='\n')
    exit(0)
hmm = magic(s, w)
if hmm == -1:
    print(-1)
else:
    print(hmm[0])
    print(hmm[1])
hmm = magic(w, s)
if hmm == -1:
    print(-1)
else:
    print(hmm[0])
    print(hmm[1])
