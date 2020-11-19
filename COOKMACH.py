for _ in range(int(input())):
    a, b = map(int, input().split())
    c = 0
    while a != b:
        if a > b:
            a >>= 1
        else:
            b >>= 1
        c += 1
    print(c)