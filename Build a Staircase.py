n, k = int(input()), int(input())
start = n // k - k
while 1:
    sm = start
    orig = sm
    for i in range(k - 1):
        sm += start + (2 * (i + 1))
    if sm == n:
        print(*[orig + 2 * i for i in range(k)], sep='\t')
        exit(0)
    if sm > n:
        print("Cannot be built"); exit(0)
    start += 1
