for _ in range(int(input())):
    x, y, l, r = map(int, input().split())
    if x == 0 or y == 0:
        print(0)
    else:
        maxi = x | y
        