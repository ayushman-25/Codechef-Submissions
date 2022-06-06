a, b, c, n = int(input()), int(input()), int(input()), int(input())
print(*[format((-c - a * i) / b, '.2f') for i in range(1, n << 1, 2)], sep='\n')
