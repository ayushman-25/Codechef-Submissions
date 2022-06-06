a, b, c, n = int(input()), int(input()), int(input()), int(input())
print(*[format((-c - a * x) / b, '.2f') for x in range(1, n << 1, 2)], sep='\n')