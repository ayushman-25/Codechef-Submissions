n, m = int(input()), float('inf')
for i in range(1, n + 1):
    if not(n % i):
        if i + n / i - 2 <= m:
            m = i + n / i - 2
    if n / i < i: break
print(int(m))
