from collections import defaultdict
n, gs, rank = int(input()), defaultdict(lambda: list()), 1
for _ in range(n):
    a, b, c, d = list(map(str, input().split()))
    gs[int(b) * 10 + int(c) * 30 + int(d) * 50].append(a)
for s in sorted(list(gs.keys()), reverse=True):
    print(*["   ".join([str(rank), i]) for i in sorted(gs[s])], sep='\n')
    rank += len(gs[s])
