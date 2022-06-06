for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    floors = [int(i) for i in input().split()]
    minans = int(1e18)
    for i in floors:
        temp = abs(b - i) + c + abs(i - a)
        if temp < minans:
            minans = temp
    print(minans)