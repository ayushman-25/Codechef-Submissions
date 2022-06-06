n, a, b = int(input()), int(input()), int(input())
print(min(max(i * a, (n - i) * b) for i in range(n)))
