from collections import defaultdict

def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0): return 0
    return 0 if (n == 1) else 1

n, tok, dd = int(input()), list(map(int, input().split())), defaultdict(lambda: list())
for [a, b] in sorted([list(map(int, input().split())) for _ in range(n - 1)]):
    dd[a].append(b); [dd[j].append(b) for j in dd.keys() if (a in dd[j])]
print(*[sum(isprime(tok[i - 1]) for i in dd[int(input())]) for _ in range(int(input()))], sep='\n')