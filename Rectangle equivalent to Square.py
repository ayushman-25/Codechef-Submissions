n = int(input())
print(len(list(filter(lambda i: not n % i, range(1, n + 1)))) >> 1)
