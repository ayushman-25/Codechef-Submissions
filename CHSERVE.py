for _ in range(int(input())):
    p1, p2, k = map(int, input().split())
    print("COOK" if ((p1 + p2) // k) & 1 else "CHEF")