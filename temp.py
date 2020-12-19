from math import log2
for _ in range(int(input())):
    n = int(input())
    if(log2(n) == int(log2(n))):
        print(*[i for i in range(1, n + 1)])
        continue
    if(n == 1):
        print(1)
        continue
    else:
        ans = []
        temp = 2 ** int(log2(n)) + 1
        for i in range(temp, n + 1):
            ans.append(i)
        for i in range(1, temp):
            ans.append(i)
        print(*ans)