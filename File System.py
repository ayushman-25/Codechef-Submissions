adj = [[] for _ in range(int(input()))]
for _ in range(int(input())):
    x, y = map(int, input().split())
    adj[x - 1].append(y)
s = list(map(str, input().split()))
for _ in range(int(input())):
    tl = [i.split('/')[1:] if '/' in i and i != '/' else i for i in list(map(str, input().split()))]
    print("no" if tl[-1] in [s[k - 1] for k in adj[s.index(tl[1][-1])]] else "yes")
