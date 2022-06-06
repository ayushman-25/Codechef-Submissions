for _ in range(int(input())):
    n = int(input())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    A, B = sum(a), sum(b)
    sumsa, sumsb = [], []
    tempa, tempb = 0, 0
    for i in range(n):
        tempa += a[i]
        sumsa.append(tempa)
    for i in range(1, n):
        tempb += b[i - 1]
        sumsb.append(B - tempb)
    sumsb.append(0)
    ans = 0
    for i in range(n):
        sum1 = sumsa[i] + sumsb[i]
        if ans < sum1: ans = sum1
    print(max(ans, A, B))