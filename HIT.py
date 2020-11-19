# cook your dish here
def sol(n, l):
    if l[n]==l[n-1] or l[n*2]==l[n*2-1] or l[n*3]==l[n*3-1]:
        print(-1)
        return
    
    else:
        print(l[n],l[n*2],l[n*3])
    
for t in range(int(input())):
    n = int(input())//4
    l = sorted(list(map(int,input().split())))
    sol(n,l)