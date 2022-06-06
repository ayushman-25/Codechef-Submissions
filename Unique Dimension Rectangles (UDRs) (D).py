n = int(input())
ans = [(i, i) if (i * i == n) else (i, n // i) for i in range(1, int(n ** 0.5) + 1) if (n % i == 0)]
print(len(ans), *[" ".join([str(j) for j in i]) for i in ans], sep='\n')