for _ in range(int(input())):
    c, d, l=map(int,input().split())
    ma=c * 4 + d * 4
    mi=d * 4 + max(0, (c - 2 * d) * 4)
    print("yes" if(l >= mi and l <= ma and l % 4 == 0) else "no")