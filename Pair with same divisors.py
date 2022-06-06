n = int(input())
print(sum(a * b == n and sum(a % i == 0 for i in range(1, a + 1)) == sum(b % i == 0 for i in range(1, b + 1)) for b in
          range(1, n) for a in range(1, b)) if n > 1 else -1)
