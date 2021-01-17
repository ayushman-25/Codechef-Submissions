u, l = int(input()), int(input())
print(len(set([i / j for j in range(l, u + 1) for i in range(l, u + 1) if(0.2 < i / j < 0.6 and gcd(i, j) == 1)])))
