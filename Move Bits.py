n, m = int(input()), int(input()) - 1
print(n >> m if (n & (1 << m)) else n << m)