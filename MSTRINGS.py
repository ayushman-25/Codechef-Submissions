for i in range(int(input())):
    st = input()
    flag = 0
    for i in range(len(st)):
        ans = st[i] 
        for j in range(i + 1, len(st)):
            ans=ans + st[j]
            co = "".join(reversed(ans))
            if(co not in st):
                flag = 1;
                break
        if(flag == 1):
            break
    if(flag == 0):
        print("YES")
    else:
        print("NO")
                
            
   
        
    