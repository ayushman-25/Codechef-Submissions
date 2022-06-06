def fact (n):
    fa = 1
    if n == 0 and n==1:
        return 1
    else:
        for i in range(n):
            fa = fa * (i + 1)
        return fa
        
for _ in range(int(input())):
    
    a = sorted(list(map(int,input().split())))[::-1]
    k = int(input())
    b = []
    b = a[:k]
    c1 = b.count(b[-1])
    c2 = a.count(b[-1])
    if(c2 == 0):
        print(1)
    else:
        print(fact(c2) // (fact(c2 - c1) * fact(c1)))