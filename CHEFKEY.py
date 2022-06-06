for __ in range(int(input()))
    n, m, c = map(int, input().split())
    count = 0
    for i in range(1, n + 1):
        if c % i == 0 and c // i <= m: count += 1
    print(count)