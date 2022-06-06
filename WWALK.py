for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    dista = [0]
    distb = [0]
    for i in range(n):
        dista.append(dista[-1] + a[i])
        distb.append(distb[-1] + b[i])
    sum1 = 0
    for i in range(1, n + 1):
        if((dista[i] == distb[i]) and (dista[i - 1] == distb[i - 1])):
            sum1 += (dista[i] - dista[i - 1])
    print(sum1)