for i in range(int(input())):
    n, k = map(int,input().split())
    j = 1
    m = 1
    flag = 0
    while(m <= n):
        j = m
        m = m + 3 
        if((j <= k and k < m) and (j <= k + 1 and k + 1 < m)):
            flag = 1
            break
    if(flag == 1):
        print("yes")
    else:
        print("no")