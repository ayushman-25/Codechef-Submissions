from collections import Counter

for _ in range(int(input())):
    n = int(input())
    sticks = list(map(int, input().split()))
    c = Counter(sticks)
    a = -1
    b = -1
    for i in sorted(c.keys(), reverse = True):
        if(c[i] >= 2):
            pairs = c[i] // 2
            
            if(pairs >= 2):
                if(a == -1):
                    a = i
                if(b == -1):
                    b = i
                    break
            else:
                if(a == -1):
                    a = i
                else:
                    b = i
                    break
    if(a == -1 or b == -1):
        print(-1)
    else:
        print(a * b)