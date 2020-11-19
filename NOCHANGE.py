def checkm(l1, p):
    if all(p % i == 0 for i in l1):
        return 1
    return 0


for _ in range(int(input())):
    n, p = map(int, input().split())
    l1 = [int(i) for i in input().split()]
    if checkm(l1, p):
        print("NO")
    else:
        
