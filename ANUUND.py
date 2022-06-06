for __ in range(int(input())):
    n=int(input())
    a=[]
    a=list(map(int,input().split()))
    a.sort()
    
    for j in range(1,n-1,2):
            a[j],a[j+1]=a[j+1],a[j]
        
    print (' '.join(map(str,a)))