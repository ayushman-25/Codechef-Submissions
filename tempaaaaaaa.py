'''class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            initialAge=0
            print ('Age is not valid, setting age to 0')
            age=initialAge#  some more code to run some checks on initialAge
    def amIOld(self):
        if intialAge<13:
            print ('You are young.')
        elif 13<=initialAge<18;:
            print ('You are a teenager.')
        else:
            print ('You are old.')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        initalAge=intialAge+1# Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
    '''
'''import math
import os
import random
import re
import sys
import numpy


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    x=(arr[::-1])
    print (" ".join(str(e) for e in x))'''
'''    
n = int(input())
    integer_list = map(int, input().split())
    y=tuple(integer_list)
    print hash(y)'''

'''
s=input()
for i in s:
    if i.islower()==True:
        i=i.upper()
        print (i,end='')
    elif i.isupper()==True:
        i=i.lower()
        print (i,end='')
    else:
        pass
'''
'''s=input()
print (''.join([i.lower() if i.isupper() else i.upper() for i in s])
'''
'''def mutate_string(string, position, character):
    string = string[:5]+character+string[6:]
    return (string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print (s_new)'''
'''
for i in range(int(input())):
    a,b,c,d=input().split()
    b=float()
    c=float()
    d=float()
    print max(b+c+d)
 '''

'''# cook your dish here
import sys
x,y=(input().split())
X=int(x)
Y=float(y)
if 0<X<=2000 and 0.00<Y<=2000.00:
    if X%5!=0 or X>Y:
        print (format(Y,'.2f'))
    else:
        z=Y-(X+0.5)
        print (format(z,'.2f'))
else:
    sys.exit()'''
'''
test_cases=int(input())
i=0
for i in range(0,test_cases):
    a,b = input().split()
    a=int(a)
    b=int(b)
    print (a+b)
    i+=1    
    '''
'''  
lines,div=map(int,input().split(' '))
count=0
for N in range(lines):
    a=int(input())
    if a%div==0:
        count+=1
print (count)'''
'''
test_cases=int(input())
for i in range(test_cases):
    a=int(input())
    N=0
    for N in range(1,a):
        a=a*N
        N+=1
    print (a)'''
'''  
test_cases=int(input())
for i in range(test_cases):
    a=input()
    b=0
    sum=0
    for i in a:
        i=int(i)
        sum=sum+i
        b+=1
    print (sum)
'''
'''
test_cases=int(input())
l=[]
for N in range(test_cases):
    a=int(input())
    l.append(a)
l.sort()
for i in l:
    i=int(i)
    print(i)
'''
'''
test_cases=int(input())
for N in range(test_cases):
    a,b=input().split()
    a=int(a)
    b=int(b)
    z=a%b
    print (z)     
        
'''
'''
test_cases=int(input())
for N in range(test_cases):
    a=input()
    a1=int(a[0])
    a2=int(a[-1])
    print (a1+a2)
 '''
'''
rounds=int(input())
l=[]
for N in range(rounds):
    p1,p2=input().split()
    p1=int(p1)
    p2=int(p2)
    l.append(p1-p2)
l.sort()
if abs(l[0])>l[-1]:
    z=abs(l[0])
    print ('2',z,end='')
else:
    z1=l[-1]
    print ('1',z1,end='')
'''

'''    
test_cases=int(input())
for N in range(test_cases):
    a=input()
    count = 0
    for i in a:
        i=int(i)
        if i==4:
            count+=1
    print (count)
'''
'''
test_cases = int(input())
for N in range(test_cases):
    number=input()
    rev_num=number[::-1]
    rev_num=int(rev_num)
    print (rev_num)'
'''
'''
print ('help')
'''
'''
import math
test_cases=int(input())
for N in range(test_cases):
    a=int(input())
    b=math.sqrt(a)
    b=b//1
    print (format(b,'.0f'))
'''
'''
test_cases=int(input())
l=[]
for n in range(test_cases):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    print (l[1]) 
print (l)'''
'''
test_cases=int(input())
for N in range(test_cases):
    a=int(input())
    if a==0:
        print (1)
    else:
        for i in range(1,a):
            a=a*i
        print (a)'''
'''        
test_cases=int(input())
for N in range(test_cases):
    a,b,c=map(int,input().split())
    _pow=a**b
    e=round(_pow/c)
    a1=int(c*e)   #possible answer 1
    a2=int(c*(e+1)) #possible answer 2
    
    if (a==b) and (b==c):
        print ((a**b)-c)
        break
    if (_pow-a1)<=(a2-_pow):
        print (a1)
    else:
        print (a2)
'''
'''
test_cases = int(input())
for N in range(test_cases):
    number=int(input())
    x=number//2
    while x>1 or number==1:
        if number%x==0:
            print ('no')
            break
        x=x-1
    else:
        print ('yes')
        
'''
'''
for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    b.sort()
    print (b)
    sum = b[0] + b[1]
    print (sum)
'''
'''
for _ in range(int(input())):
    a,b,c = map(int,input(),split())
    if a+b+c=180:
        print ("YES")
    else:
        print ("NO")
'''
'''
for _ in range(int(input())):
    a=list(map(int,input().split()))
    m=[]
    b=min(a)
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            m.append(i)
    hcf = (max(m))
    lcm = int((a*b)/hcf)
    print (hcf,lcm,end='')
'''
'''
for _ in range(int(input())):
    D,N = map(int,input().split())
    i=0
    sum1=0
    for i in range(1,N+1):
        sum1=sum1+i
        i+=1
    g=0
    sum2=0
    for g in range(1,sum1+1):
        sum2=sum2+g
        g+=1
    h=0
    sum3=0
    for h in range(1,sum2+1):
        sum3=sum3+h
        h+=1
    j=0
    sum4=0
    for j in range(1,sum3+1):
        sum4=sum4+j
        j+=1
    if D==1:
        print (sum1)
    elif D==2:
        print (sum2)
    elif D==3:
        print (sum3)
    else:
        print (sum4)
'''
'''
chr1=input()
if chr1 in 'aeiouAEIOU':
    print ('Vowel')
else:
    print ('Consonant')
    
'''
'''
for _ in range(int(input())):
    l=[]
    L=[]
    N=int(input())
    n1 = 0
    n2 = 1
    for num in range(1,N):
        if num<=1:
            nth=num
        else:
            nth=n1+n2
            n1,n2=n2,nth
        l.append(nth)
    for i in l:
        L.append(i%10)
    while len(L)>1:
        del L[0::2]
    print (L[0])
            
'''

'''
for _ in range(int(input())):
    N,K = map(int,input().split())
    seq = list(map(int,input().split()))
    for i in range(seq):
    
for i in range(5):
    a=int(input())
    if a==42:
        break
    else:
        print (a)

import time
start = time.time()
test_Cases=int(input())
for N in range(test_Cases):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        x=i//2
        while x>1:
            if i%x==0:
                break
            x-=1
        else:
            print (i)
end=time.time()
print (end - start)

import time
start = time.time()
l=[]
for i in range(5):
    l.append(i**i)
print (l)

a=[i**i for i in range(5)]
print (a)

end = time.time()
print (end - start)       
'''
'''   
import sys
A=[]
B=[]
f=0
for _ in range(int(input())):
    a=input()
    b=input()
    for i in a:
        A.append(i)
    for i in b:
        B.append(i)
    A.sort()
    B.sort()
    if len(A)!=len(B):
        print ('Strings are not anagram')
    else:
        for i in range(0,len(a)):
            if A[i] == B[i]:
                f=1
            else:
                f=2
        if f==1:
            print ('Strings are anagram')
        elif f==2:
            print ('Strings are not anagram')
'''
'''
for _ in range(int(input())):
    l=[]
    N,K=map(int,input().split())
    Ai=list(map(str,input().split()))
    print (Ai)
    res=str("".join(map(str,Ai)))
   
    def printAllKLengthRec(Ai,prefix,n,K):
        if K == 0:
            print (prefix)
            return
        for i in range(n):
            newPrefix = prefix + Ai[i]
            l.append(newPrefix)
            printAllKLengthRec(Ai,newPrefix,n,K-1)
    def printAllKLength(Ai,K):
        n=len(Ai)
        printAllKLengthRec(Ai,"",n,K)
    (printAllKLength(Ai,K))
    print (l)
    for i in l:
        i=int(i)
    for i in l:
        for j in range(i):
            print (j)
'''
'''
for _ in range(int(input())):
    a1,a2,a3,c1,c2,c3=map(int,input().split())
    if a1==a2 and c1==c2 and c3>c2 and c3>c1:
        print('FAIR')
        
    elif a1==a3 and c1==c3 and c2>c1 and c2>c3 and c1==c3:
        print('FAIR')
        
    elif a3==a2 and c3==c2 and c1>c3 and c1>c2:
        print('FAIR')
        
    elif a1>a2 and a2>a3 and c1>c2 and c2>c3:
        print('FAIR')
        
    elif a2>a1 and a2>a3 and c2>c1 and c2>c3:
        print('FAIR')
        
    elif a3>a1 and a3>a2 and c3>c1 and c3>c2:
        print('FAIR')
      
    else:
        print ('NOT FAIR')
'''
'''       
n=int(input())
n=str(n)
L=[]
l=[]

for i in n:
    n=int(n)
    i=int(i)
    L.append(i)
    if n%i==0:
        l.append(i)
    else:
        pass
if all(n%i!=0 for i in L)==True:
    print ('No factors')
else:
    x=l[::-1]
    x=str(x)[1:-1]
    print (x)
    
'''
'''
x,y=(input().split())
X=int(x)
Y=float(y)
if 0<X<=2000 and 0.00<=Y<=2000.00:
    if X%5==0 and Y>X+0.50:
        print (format(Y-X-0.50,'.2f'))
    else:
        print (format(Y,'.2f'))
else:
    pass
'''
'''
places=int(input())
l=[]
ml=[]
for _ in range(places):
    litres=int(input())
    l.append(litres)
    millilitres=int(input())
    ml.append(millilitres)
sum1=0
i=0
for i in l:
    sum1+=i
    i+=1
sum2=0
j=0
for j in ml:
    sum2+=j
    j+=1
if (sum2)<1000:
    print(sum1)
    print (sum2)
else:
    b=int(sum2//1000)
    c=sum2%1000
    print (sum1+b)
    print (c)
'''
'''
for _ in range(int(input())):
    s=input()
    l=[]
    L=[]
    l1=[]
    l2=[]
    if len(s)%2==0:
        a=0
        for i in s:
            l.append(i)
        for i in s:
            L.append(i)
            
        del l[len(s)//2::]
        del L[0:len(s)//2]
        l.sort()
        L.sort() 
        if l==L:
            print ('YES')
        else:
            print ('NO')
    else:
        a=1
        for i in s:
            l1.append(i)
        for i in s:
            l2.append(i)
        del l1[len(s)//2::]
        del l2[0:(len(s)//2)+1]
        l1.sort()
        l2.sort()
        if l1==l2:
            print ('YES')
        else:
            print ('NO')
'''
'''
    if a==0:
        for i in l:
            if i in L:
                b=1
            else:
                c=1
    elif a==1:
        for i in l1:
            if i in l2:
                d=1
            else:
                e=1
    else:
        pass
    if b==1 or d==1:
        print ('YES')
    elif c==1 or e==1:
        print ('NO')
    else:
        pass
                

l.append(s[0:len(s)//2])
        L.append(s[len(s)//2::])
        
l1.append(s[0:len(s)//2])
        l2.append(s[c])

'''
'''
for _ in range(int(input())):
    q,p=(input().split())
    q=int(q)
    p=int(p)
    if q<=100:
        print (format(q*p,'.6f'))
    else:
        z=(q*p)-((q*p)/10)
        print (format(z,'.6f'))
'''
'''
l=[]
for _ in range(int(input())):
    a=int(input())
    b=int(input())
    c=int(input())
    l.append(a+b+c)
l.sort()
print (l[::-1])
'''
'''
F=int(input())
H=int(input())
D=int(input())
l=[]
L=[]
N=int(input())
for _ in range(N):
    Da=int(input())
    La=int(input())
    l.append(Da)
    l.append(La)
for i in range(len(l)):
    if l[i]==D:
        L.append(l[i+1])
L.sort()
'''
'''
F=int(input())
H=int(input())
D=int(input())
l=[]
L=[]
L1=[]
f=0
N=int(input())
for _ in range(N):
    Da=int(input())
    La=int(input())
    l.append(Da)
    l.append(La)
for i in range(len(l)):
    if l[i]==D:
        L.append(l[i+1])
L.sort()
if len(L)%2==0:
    f=0
    sum1=0
    i=0
    for i in L:
        sum1+=i
        i+=1
        L1.append(sum1)
        L1.append()
'''
'''
F=int(input())
H=int(input())
D=int(input())
l=[]
L=[]
N=int(input())
for _ in range(N):
    Da=int(input())
    La=int(input())
    l.append(Da)
    l.append(La)
for i in range(len(l)):
    if l[i]==D:
        L.append(l[i+1])
L.sort()
if len(L)%2!=0:
    s=0
    x=len(L)
    c=0
    for i in range(0,x+2,2):
        s=L[i]+L[i+1]
        c+=s
        L.append(s)
        x+=1
    print (c)
else:
    pass
'''
'''
f=int(input())
h=int(input())
d=int(input())
n=int(input())
l1=[]
l2=[]
dx=0
ln=0
for i in range(n):
    dx=int(input())
    ln=int(input())
    l1.append(dx)
    l2.append(ln)
l3=[]
for i in range(len(l1)):
    if l1[i]==d:
        l3.append(l2[i])
print (l3)
    
s=0
x=len(l3)
c=0
for i in range(0,x+2,2):
    l3.sort()
    s=l3[i]+l3[i+1]
    c+=s
    l3.append(s)
    x+=1
print (c)
'''
'''
l=[1,1,2,4]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print (l1)
'''
'''
a=int(input())
j=0
if a==0 or a==1 or a==2:
    print ('impossible')
else:
    for i in range(0,a):
        for j in range(i,a):
            print ("*",end='')
        for j in range(0,2*i+1):
            print (" ",end='')
        for j in range(i,a):
            print ("*",end='')
        print ()
    for i in range(0,a-1):
        for j in range(0,i+2):
            print ("*",end='')
        for j in range(0,2*(a-1-i)-1):
            print (" ",end='')
        for j in range(0,i+2):
            print ("*",end='')
        print ()
 '''
'''
for _ in range(int(input())):
    c,l=map(int,input().split())
    a=list(map(int,input().split()))
z=0
L=[]
for i in a:
    z+=1
for start in range(z):
    for end in range(1,z+1):
        l=a[start:end]
        L.append(l)
print (L)
d=0
for i in L:
    d+=1
f = 0
for i in L:    
  for start in range(z):
  for end in range(1, z+1):
    s = sum(l[start:end]) 
    if s < f: 
        f = s
print (f)
'''
'''
L=[]
sublist =[]
for i in range(z + 1): 
    for j in range(i + 1, z + 1):
        sub = a[i:j] 
        sublist.append(sub)   
L.append(sublist) 
print (L)
'''
''' 
Ll=[]
for i in L:
    Ll.append(i)
L1=[]
for i in Ll:
    for j in i:
        L1.append(j)
LL=[]
for i in L1:
    x=0
    for j in i:
        x+=1
    if x==l:
        LL.append(i)

'''
'''
L2=[]
for i in LL:
    print (i)
    for j in i:
        sum1=0
        print (j)
        sum1+=j
        j+=1
        L2.append(j)
print (L2)
'''
'''
import time 
start=time.time()
for _ in range(int(input())):
    d=int(input())
    if d<10:
        print (d+1)
    else:
        sum1=0
        f=0
        d=str(d)
        for i in d:
            i=int(i)
            sum1+=i
            i+=1
        print (sum1)
end=time.time()
print (end - start)
'''
'''
for _ in range(int(input())):
    a,b=map(int,input().split())
    flag=0
    for i in range(a,b+1):
        i=str(i)
        if i[-1]=='2' or i[-1]=='3' or i[-1]=='9':
            flag+=1
            else:
                pass
    print (flag)
'''
'''    
for _ in range(int(input())):
    a=int(input())
    b=int((a/4)-1)
    print (b)
    
'''
'''
for _ in range(int(input())):
    l=[]
    number1,number2=map(int,input().split())
    if number1==1:
        number1=number1+1
    else:
        pass
    for number in range(number1,number2+1):
        x=number//2
        while x>1:
            if number%x==0:
                break
            x=x-1
        else:
            l.append(number)

for i in l:
    print (i)
'''
'''
a=int(input())
b=int(input())
z=a-b
print (z)
z=str(z)
z=list(z)
for i in range(len(z)):
    z[-1]='1'
for i in z:
    i=int(i)
    print (i,end='')
'''
'''
N=int(input())
N=str(N)
for i in range(len(N)):
    i=int(i)
    n=int(N[0:i])
    print (n)
'''
'''
N=int(input())
N=str(N)
L=[]
l=[]
f=0
for i in range(len(N)): 
    L.append(N[0:i+1])
for i in range(len(N)):
    l.append(len(N)-i)
for i in range(len(L)):
    L[i]=int(L[i])
if all(L[i]%l[i]==0 for i in range(len(L)))==True:
    print ('Yes')
else:
    print ('No')

    L.append(N[0:i+1])
    break
print (L)
if all(n%i!=0 for i in L)==True
'''
'''
L1=[]
L2=[]
n=input()
Lfirst = n[0 : 1] 
Lsecond = n[1 :] 
print(Lsecond)
print(Lfirst)
L1.append(Lsecond+Lfirst)
n=Lsecond+Lfirst 
Lfirst = n[0 : 1] 
Lsecond = n[1 :]   
L1.append(Lsecond+Lfirst)
n=Lsecond+Lfirst 
Lfirst = n[0 : 1] 
Lsecond = n[1 :]   
L1.append(Lsecond+Lfirst)
n=Lsecond+Lfirst 
Lfirst = n[0 : 1] 
Lsecond = n[1 :]  
L1.append(Lsecond+Lfirst)
for i in range(len(L1)):
    L1[i]=int(L1[i])
for i in L1:
    for j in range(1,i):
        if i%j==0:
            L2.append(j)
        else:
            pass
print (x)
for i in L1:
    if i%x==0:
        print (i)
    else:
        pass
'''
'''
import time
start=time.time()
n=input()
n1=int(n)%(10**(len(n)-1))
n2=int(n)//(10**(len(n)-1))
print ((n1*10)+n2)
end=time.time()
print (end - start)
'''
'''
L=[]
n=int(input())
a=int(input())
b=int(input())
for i in range(1,n):
    l=[]
    A=i
    B=n-i
    if a*A==b*B:
        l.append(a*A)
        l.append(b*B)
        Aa=max(l)
        L.append(Aa)
for i in L:
    print (i)
'''
'''
n=int(input()) 
t=int(input())
u=int(input())
temp=0
j=1
while j>=1:
    if j%t==0:
        temp=temp+1
    elif j%u==0:
        temp=temp+1
    elif temp==1:
        print (j)
        break
    j=j+1
    
print (22)
'''
'''
import math
k=int(input())
x=1
y=math.factorial(x)
while y<k:
    x=x+1
    y*=x
print (x)
if y==k:
    if x%2==0:
        fact=1
        for i in range(2,x+1,2):
            fact=fact*i
        print (fact)
    else:
        fact=1
        for i in range(1,x+1,2):
            fact*=i
        print (fact)
            
else:
    print (-1)

'''
'''
x=list(input())
y=list(input())
a=[]
b=[]
for i in y:
    b.append(i)
for i in x:
    a.append(i)
    if i in y:
        x.remove(i)
        y.remove(i)
for i in range(len(x)):
    x[i]=int(x[i])
for i in range(len(y)):
    y[i]=int(y[i])
if x==[]:
    if y==['0']:
        x=-1
        print (format(x,'.2f'))
    else:
        for i in a:
            if i in b:
                b.remove(i)
                s1=[str(i) for i in a]
                s2=[str(i) for i in b]
                ress1=int("".join(s1))
                ress2=int("".join(s2))
                print(ress1)
                print(ress2)
                ans1 = ress1/ress2
                print (format(ans1,'.2f'))
else:
    s=[str(i) for i in x]
    res1=int("".join(s))
    s=[str(i) for i in y]
    res2=int("".join(s))
    if res2!=0:
        ans1=res1/res2
        print (format(ans1,'.2f'))
    else:
        x=-1
        print (format(x,'.2f'))
'''
'''
x = (input())
y = (input())
if y == 0:
    print ("%2f"%(-1))
    exit(0)
x = list(x)
y = list(y)
i=0
j=0
while i < len(x):
    j=0
    while j < len(y):
        if x[i] == y[j]:
            del x[i]
            del y[j]
            i -= 1
            break
        j+=1
    i+=1
if len(x) != 0:
    x=int("".join(x))
else:
    x=1
if len(y) != 0:
    y=int("".join(y))
else:
    y = 1
if y == 0:
    print ("%.2f"%(-1))
    exit(0)
print ("%.2f" % (x/y)) 
'''
'''
test_cases = int(input())      
a=list(map(int,input().split()))
x=max(a)
x=x/2
a.remove(max(a))
a.append(x)
sum=0
i=0
for i in a:
    sum=sum+i
    i+=1
a=int(sum)
print (a)
'''
'''
import math
l = []
m = []
for _ in range(int(input())):
    a = int(input())
    l.append(a)
for i in l:
    b = int(math.log(i)/math.log(2))
    m.append(b)
i = 0
sum = 0
for i in m:
    sum += i
    i += 1
print(sum)
'''
'''
l=[]
m=[]
n=[]
o=[]
for _ in range(int(input())):
    a,b=input().split()
    a=int(a)
    l.append(a)
    m.append(b)
for i in l:
    if l.count(i)>1 and l.count(i)%2==0:
        n.append(i)
for i in m:
    if m.count(i)>1:
        o.append(i)
if len(n) > len(o):
    print (len(n)//2)
else:
    print (len(o)//2)
'''
'''
a,b,c,d = map(int,input().split())
A = a * 5
B = b * 10
C = c * 15
D = d * 20
ans = int(((A+B+C+D)/20)*500)
print(ans)
'''
'''
l=[]
for _ in range(int(input())):
    n=int(input())
    j=0
    for i in range(0,n+1):
        for j in range(1,n+1):
            l.append(i+j)
print (l)
'''
'''
N=int(input())
ans=N//3
print (ans)
'''
'''
l1=['!','@','#','$']
l2=[1,2,3,4]
l3=[]
for _ in range(int(input())):
    s=list(input())
    s=tuple(s)
    if s.count(i)>1:
            l3.append(i)
            l1.remove(i)
    print (l3)
    s=list(s)
    L3=[i for i, item in enumerate(l1) if item in s]
    for i in s:    
        sum1=0
        v=0
        for i,v in enumerate(l2):
            if i in L3:
                sum1+=v
                v+=1
    print (sum1)
    s=tuple(s)
   
'''
'''
import itertools
for _ in range(int(input())):
    a=[]
    N=int(input())
    for i in range(1,N+1):
        a.append(i)
    def contains_sublist(lst, sublst):
        n = len(sublst)
        return any((sublst == lst[i:i+n]) for i in range(len(lst)-n+1))
    b=[i for i in itertools.combinations(a,2)]
    c=[]
    for i in b:
        sum1=1
        j=1
        for j in i:
            sum1*=j
            j+=1
        c.append(sum1)
    sum2=0
    i=0
    for i in c:
        sum2+=i
        i+=1
    print (sum2)
'''

'''
    i=1
    for i in range(1,N+1):
        a.append(i*(i+1))
    if len(a)==0:
        a.append(0)
    elif len(a)>2:
        a.pop(-1)
        a.append(N)
    else:
        a.pop(-1)
    i=0
    sum1=0
    for i in a:
        sum1+=i
        i+=1
    print (sum1)
'''
'''
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    d,e,f = map(int,input().split())
    g,h,j = map(int,input().split())
    if (a+b+c)>(d+e+f) and (a+b+c)>(g+h+j) and a>=d and a>=e and a>=f and a>=g and a>=h and a>=j and b>=d and b>=e and b>=f and b>=g and b>=h and b>=j and c>=d and c>=e and c>=f and c>=g and c>=h and c>=j:
        print ('yes')
    elif (d+e+f)>(a+b+c) and (d+e+f)>(g+h+j) and d>=a and d>=b and d>=c and d>=g and d>=h and d>=j and e>=a and e>=b and e>=c and e>=g and e>=h and e>=j and f>=a and f>=b and f>=c and f>=g and f>=h and f>=j:
        print ('yes')
    elif (g+h+j)>(a+b+c) and (g+h+j)>(d+e+f) and g>=a and g>=b and g>=c and g>=d and g>=e and g>=f and h>=a and h>=b and h>=c and h>=d and h>=e and h>=f and j>=a and j>=b and j>=c and j>=d and j>=e and j>=f:
        print ('yes')
    else:
        print ('no')
'''
'''
for _ in range(int(input())):
    a,b = map(int,input().split())
    c=int((a * (a + 1) * (a + 2)) / 6)
    print (c%b)
'''
'''    
l1=['!','@','#','$']
l2=[1,2,3,4]

for _ in range(int(input())):
    s=set(input())
    L3=[i for i, item in enumerate(l1) if item in s]
    sum1=0
    v=0
    for i,v in enumerate(l2):
        if i in L3:
            sum1+=v
            v+=1
    print (sum1)
'''
'''
import itertools
l=[]
L=[]
for _ in range(int(input())):
    U,V = map(int,input().split())
    l.append(U)
    l.append(V)
print (l)
i=0
for i in range(len(l)+1):
    l=[l[i],[i+1]]
    l.append(L)
    i+=1
print (L)
'''
'''
import math    
y=int(input())
z=int(y//2)
f=0
for i in range(2,z):
    if y%i==0:
        f+=1
        break
    
if f==0:
    print ('Prime')
else:
    print ('Not a Prime')
'''
'''
test_cases=int(input())
for _ in range(test_cases):
    arr=list(map(int,input().split()))
    l=len(arr)
    a=l-1
    if a in arr:
        arr.remove(a)
    else:
        pass
    A=max(arr)
    print (A)

'''
'''
a=list(map(int,input().split()))
print (type(a))
print (a)
'''
'''
for _ in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    if a+b+c+d+e==0:
        print ('Beginner')
    elif a+b+c+d+e==1:
        print ('Junior Developer')
    elif a+b+c+d+e==2:
        print ('Middle Developer')
    elif a+b+c+d+e==3:
        print ('Senior Developer')
    elif a+b+c+d+e==4:
        print ('Hacker')
    elif a+b+c+d+e==5:
        print ('Jeff Dean')
    else:
        pass
'''
'''
for _ in range(int(input())):
    N,K = map(int,input().split())
    m = list(map(int,input().split()))
    for i in range(len(m)):
        if m[i]<K:
            print (1)
            bal=K-m[i]
        
'''
'''   
for _ in range(int(input())):
    A,B=map(int,input().split())
    s=A+B
    print (s)
    if int(s%2)==0:
        print('Limak')
    else:
        print ('Bob')
'''
'''
for _ in range(int(input())):
    l=[]
    A,B,N = map(int,input().split())
    i=0
    for i in range(1,N+1):
        A*=2
        B*=2
        i+=1
    l.append(A)
    l.append(B)
    print (l)
    a=max(l)
    b=min(l)
    ans=int(a/b)
    print (ans)
'''
'''
for _ in range(int(input())):
    arr=[]
    a=list(map(int,input().split()))
    a.sort()
    print (a)
    print (a[-1])
    for i in a:
        if a[-1]%i!=0:
            arr.append(i)
    print (arr)
    A=min(arr)
    print (A)
    print (a[-1]-A)
'''
'''
import math
x=int(input())
y=int(input())
z=(math.log(x))/(math.log(y))
print (format(z,'.2f'))
'''
'''
n=[0,1,2,3,4,5,6,7,8,9]
m=[6,2,5,5,4,5,6,3,7,6]
for _ in range(int(input())):
    l=[]
    l1=[]
    a,b=map(int,input().split())
    ans=a+b
    ans=str(ans)
    for i in ans:
        i=int(i)
        l.append(i)
    l.sort()
    for i in l:
        if i in n:
            l1.append(m[i])
    i=0
    sum1=0
    for i in l1:
        sum1+=i
        i+=1
    print (sum1)
'''
'''    
s1=list(input())
l=[]
l2=[]
s2=list(input())
f=0
for i in s2:
    if i in s1:
        f=0
        l.append(s1.index(i))
    else:
        f=1
l.sort()        
for i in l:
    l2.append(s1[i])
print (l)
print(l2)
print (s2)

if f==0:
    if l2==s2:
        print ('Yes')
    else:
        print ('No')
else:
    pass
'''
'''       
cc
if len(l1)<len(l):
    for i in range(len(l1)):
        l2.append(l1[i]+l[i])
    print (l2)
else:
    for i in range(len(l)):
        l3.append(l[i]+l1[i])
    print (l3)

'''
'''
degree1=int(input())
l=[]
for _ in range(degree1+1):
    a=int(input())
    l.append(a)
degree2=int(input())
l1=[]
l2=[]
l3=[]
for _ in range(degree2+1):
    b=int(input())
    l1.append(b)
if len(l1)<len(l):
    for i in range(len(l1)):
        l2.append(l1[i]+l[i])
    print (l2)
else:
    for i in range(len(l)):
        l3.append(l[i]+l1[i])
    print (l3)
'''
'''
degree1=int(input())
l=[]
for _ in range(degree1+1):
    a=int(input())
    l.append(a)
degree2=int(input())
l1=[]
for _ in range(degree2+1):
    b=int(input())
    l1.append(b)
l=l[::-1]
l1=l1[::-1]
l2=[]
l3=[]
if len(l1)<len(l):
    a=len(l)-len(l1)
    for x in range(a):
        l1.insert(-1,0)
    print(l)
    print(l1)
    for i in range(len(l1)):
        l2.append(l1[i]+l[i])
        l2=l2[::-1]
    print(l2)
elif len(l1)>len(l):
    a=len(l1)-len(l)
    for x in range(a):
        l.insert(-1,0)
    print (l)
    print (l1)
    for i in range(len(l)):
        l3.append(l[i]+l1[i])
        l3=l3[::-1]
    print (l3)
else:
    for i in range(len(l1)):
        l2.append(l1[i]+l[i])
        l2=l2[::-1]
    print(l2)
'''
'''
degree1=int(input())
l1=[]
for _ in range(degree1+1):
    a=int(input())
    l1.append(a)
degree2=int(input())
l2=[]
for _ in range(degree2+1):
    b=int(input())
    l2.append(b)
if len(l1)>len(l2):
    l3=[]
    diff=len(l1)-len(l2)
    for i in range(diff):
        l2.insert(0,0)
    for i in range(len(l1)):
        l3.append(l1[i]+l2[i])
    print (l3)
elif len(l1)<len(l2):
    l3=[]
    diff=len(l2)-len(l1)
    for i in range(diff):
        l1.insert(0,0)
    for i in range(len(l2)):
        l3.append(l1[i]+l2[i])
    print (l3)
else:
    l3=[]
    for i in range(len(l1)):
        l3.append(l1[i]+l2[i])
    print (l3)
'''
'''
s1=input()
s2=input()
if s2 in s1:
    print ('Yes')
else:
    print ('No')
'''
'''
l=[]
import math
upper=int(input())
lower=int(input())
for i in range(lower,upper+1):
    l.append(i)
l1=[]
print (l)
for i in range(lower,upper+1):
    for j in range(lower,upper+1):
        if math.gcd(i,j)==1 and 0.2<j/i<0.6:
            l1.append(j/i)
print (len(l1))
'''
'''
for i in range(len(l)):
    for j in range(0,len(l)):
        if l[j]>l[i]:
            if math.gcd(l[j],l[i])==1:

print (l1)  
print (len(l1))
'''
'''  
a=int(input())
b=int(input())
l1=[]
l2=[]
l3=[]
for i in range(1,a+1):
    if a%i==0:
        l1.append(i)
for i in range(1,b+1):
    if b%i==0:
        l2.append(i)
if l2>l1:
    for i in l1:
        if i in l2:
            l3.append(i)
    print (l3)
elif l2<l1:
    for i in l2:
        if i in l1:
            l3.append(i)
    print (l3)
else:
    for i in l1:
        if i in l2:
            l3.append(i)
    print (l3)
'''
'''
n=int(input())
prime = [True for i in range(n+1)]
print(prime)
p = 2
while (p * p <=n):
    if (prime[p] == True):
        for i in range(p * p, n+1, p):
            prime[i] = False
    p+=1
for p in range(2,n):
    if prime[p]:
        print (p,)
'''
'''
import math
def gcd(a,b):
    while b!=0:
        t=b
        b=a % b
        a=t
    return (a)
a=int(input())
b=int(input())
print (gcd(a,b))
'''
'''
l=[] 
f=0   
for _ in range(int(input())):
    a=int(input())
    l.append(a)
l1=[]
for i in range(1,len(l)-1):
    if l[i+1]>l[i]>l[i-1]:
        f=1
        l1.append(i+1)
    else:
        f=2
if f==2:
    print ('None')
else:
    if f==1 and l[-2]<l[-1]:
        l1.append(len(l))
        for i in l1:
            print(i,)
'''
'''
l2=[]
for i in range(1,len(l)-1):
    if l[i]<l[i+1]:
        l2.append(i)
print (l2)
for i in l1:
    if i in l2:
        print (i)          
'''
'''
l=[]
f=0
for _ in range(int(input())):
    a=int(input())
    l.append(a)
l.append(l[0])
l2=[]
for i in range(1,len(l)-1):
    if l[i-1]<l[i]<l[i+1]:
        f=1
        l2.append(i+1)
if f==1:
    for i in l2:
        print (i)
else:
    print('None')
'''
'''
l=[]
l1=[]
for _ in range(int(input())):
    x,y = map(int,input().split())
    l.append(x)
    l1.append(y)
print (l)
print (l1)
l2=[]
for i in range(len(l1)):
    if l1.count(l1[i])>1:
        l2.append(i)
l3=[]
for i in l2:
    l3.append(l[i])
A=max(l3)
B=min(l3)
ans1=int(A-B)
print (ans1)
l4=[]
for i in range(len(l)):
    if l.count(l[i])>1:
        l4.append(i)
l5=[]
for i in l4:
    l5.append(l1[i])
A=max(l5)
B=min(l5)
ans2=int(A-B)
print (ans2)    
'''
'''
#Sparse Matrix(vpropel)
l=[]
rows = int(input())
if rows == 0:
    print('Invalid input')
else:
    columns = int(input())
    if columns == 0:
        print('Invalid input')
    else:
        
        for _ in range(rows*columns):
            elements = int(input())
            l.append(elements)
        a = l.count(0)
        while 0 in l:
            l.remove(0)
        print(l)
        if a >= len(l):
            print('Sparse')
        else:
            print('Not sparse')
'''
'''
s1=list(input())
s2=list(input())
for i in s1:
    while s1.count(i)>1:
        s1.remove(i)
print(s1)
'''
'''
for _ in range(int(input())):
    f=0
    l=[]
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    if len(a)%N==0:
        pass
    else:
        a.remove(a[-1])
    avg = len(a) / float(N)
    out = []
    last = 0.0

    while last < len(a):
        out.append(a[int(last):int(last + avg)])
        last += avg
    print(out)
'''
'''
word=list(input())
if all(word.count(i)==1 for i in word)==True:
    print('Good')
else:
    print('bad')
'''
'''   
word=(input())
word=word.lower()
word=list(word)
set1=set(word)
if len(set1)==len(word):
    print('Good')
else:
    print('Bad')
'''
'''
a=0
word=input()
word=word.lower()
word=list(word)
up=['q','w','e','r','t','y','u','i','o','p']
md=['a','s','d','f','g','h','j','k','l']
lw=['z','x','c','v','b','n','m']
if all(i in up for i in word)==True: print('Yes')
elif all(i in md for i in word)==True: print('Yes')
elif all(i in lw for i in word)==True: print('Yes')
else: print('No')
'''
'''
a,b=map(int,input().split())
for _ in range(a):
    c=int(input())
    if c<b: print('Bad boi')
    else: print('Good boi')
'''
'''
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a < b: print('<')
    elif a > b: print('>')
    else: print('=')
'''
'''
for _ in range(int(input())):
    z=0
    a,b=map(int,input().split())
    list1=list(map(int,input().split()))
    sublist=[[]]
    for i in range(len(list1) + 1):
        for j in range(i+1,len(list1)+1):
            sub=list1[i:j]
            sublist.append(sub)
    l=[]
    for i in sublist:
        for j in i:
            if len(i)==2:
                l.append(i)
            else: pass
        print(sublist)
    for i in l:
        print(i)
        for j in range(len(i)):
            if i[0]+i[1]==b:
                z=1
            break
    if z==1: print('Yes')
    else: print('No')
'''
'''
import itertools
for _ in range(int(input())):
    l=[]
    z=0
    a,b=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=list(itertools.combinations(list1,2))
    for i in list2:
        for j in range(len(i)):
            if i[0]+i[1]==b:
                z=1
            break
    if z==1: print('Yes')
    else: print('No')
'''
'''
import math
for _ in range(int(input())):
    l=[]
    N=int(input())
    for i in range(N):
        fib = (((1 + math.sqrt(5))**i) - ((1 - math.sqrt(5))**i)) / ((2**i) * math.sqrt(5))
        fib=int(fib)
        l.append(fib)
    for n,i in enumerate(l):
        if i>=10:
            i=i%10
            l[n] = i
    while len(l)>1:
        del l[0::2]
    print (l[0])
'''
'''
for _ in range(int(input())):
    l=[]
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    for i in A:
        b=P-i
        P=b
        l.append(b)
    L=[]
    for i in l:
        if i>0:
            L.append(i)
    print (len(L))
'''
'''
for _ in range(int(input())):
    L,R = map(int,input().split())    
    n=[]
    i=0
    l=[1,2,3,4]
    for i in range(R):
        m=1
        for i in l:
            m*=i
        n.append(m)
        i=i+1
        for i in range(len(l)):
            l[i]=l[i]+1
    N=[]
    for i in range(L-1,R):
        N.append(n[i])
    sum1=sum(N)
    print(sum1%1000000007)
'''
'''
for i in range(int(input())):
    N = int(input())
    list1 = list(map(int,input().split()))
    if len(list1)%2==0:
        print (-1)
    else:
        for i in list1:
            if list1.count(i)==1:
                print(i)
'''
'''
for _ in range(int(input())):
    ing1 = list(map(str,input().split()))
    ing2 = list(map(str,input().split()))
    set1=set(ing1+ing2)
    if len(set1)-len(ing1)<=2:
        print('similar')
    else:
        print('dissimilar')
'''
'''
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a < 1000: print (format(a*b,'.6f'))
    else: print(format((a*b)-(1*(a*b)/10),'.6f'))
'''
'''
for _ in range(int(input())):
    a=int(input())
    list1=list(map(int,input().split()))
    l1=[]
    l2=[]
    if len(list1)%2!=0:
        for i in range(0,int(len(list1)/2)):
            l1.append(list1[i])
        for i in range(int(len(list1)/2)+1,len(list1)):
            l2.append(list1[i])
        l2.sort()
        if l1==l2 and list1[int(len(list1)/2)-1]-list1[int(len(list1)/2)]==-1: print('yes')
        else: print('no')
    else: print('no')
'''
'''
for _ in range(int(input())):
    l=[]
    for i in range(int(input())):
        a=int(input())
        l.append(a)
    for i in l: 
        if l.count(i)==1: print(i)
'''
'''
import itertools
for _ in range(int(input())):
    l=[]
    a=int(input())
    list1=list(map(int,input().split()))
    b=list(itertools.combinations(list1,2))       
    for i in b:
        for j in i:
            c=i[0]-i[1]
            l.append(c)
    l1=[]
    for i in l:
        if i > 0:
            l1.append(i)
    print(l1)
    a=min(l1)
    print(a)
'''
'''
for _ in range(int(input())):
    a,b = map(int,input().split())
    list1 = list(map(int,input().split()))
    c=0
    for i in list1:
        if i >= b:
            c+=1
    print(c)
'''
'''
for _ in range(int(input())):
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    list3=list(map(int,input().split()))
    summ=[]
    sum1=sum(list1)
    sum2=sum(list2)
    sum3=sum(list3)
    summ.append(sum1)
    summ.append(sum2)
    summ.append(sum3)
    for i in summ:
        if summ.count(i)>1:
            f=1
    if f==1:
        print('no')
    else:
        i=summ.index(max(summ))
        if i==0:
            if list1[0]>=list2[0] and list1[1]>=list2[1] and list1[2]>=list2[2] and list1[0]>=list3[0] and list1[1]>=list3[1] and list1[2]>=list3[2]:
                print('yes')
            else:
                print('no')
        elif i==1:
            if list2[0]>=list1[0] and list2[1]>=list1[1] and list2[2]>=list1[2] and list2[0]>=list3[0] and list2[1]>=list3[1] and list2[2]>=list3[2]:
                print('yes')
            else:
                print('no')
        elif i==2:
            if list3[0]>=list2[0] and list3[1]>=list2[1] and list3[2]>=list2[2] and list3[0]>=list1[0] and list3[1]>=list1[1] and list3[2]>=list1[2]:
                print('yes')
            else:
                print('no')
        else:
            pass
'''
'''
for _ in range(int(input())):
    a=int(input())
    c=0
    if a==1 or a==0:
        print(-1)
    else:
        for i in range(100000):
            if a%10!=0:
                a*=2
                c+=1
            i+=1
    print(c)

'''
'''
import math
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    print(math.gcd((a**c+b**c),(a-b)))
'''
'''
N = input()
if len(N)==1: print(1)
elif len(N)==2: print(2)
elif len(N)==3: print(3)
else: print('More than 3 digits')
'''
'''
#S10E(codechef, OCT10B)
for _ in range(int(input())):
    a = int(input())
    l1 = list(map(int,input().split()))
    good = 1
    for i in range(1,5):
        if all(l1[i]<l1[j] for j in range(0,i))==True:
                good += 1
    for i in range(5,len(l1)):
        if all(l1[i]<l1[j] for j in range(i-5,i))==True:
            good += 1
    print(good)
'''

'''
#MARM(codechef, OCT19B)
for _ in range(int(input())):
    N,K = map(int,input().split())
    list1 = list(map(int,input().split()))
    for i in range(K):
        a = list1[i%N]
        b = list1[N-(i%N)-1]
        list1[i%N] = (a^b)
    for i in list1:
        print (i,end=' ')
'''
'''
#ADDREV(spoj)
for _ in range(int(input())):
    a,b = map(str,input().split())
    a = a[::-1]
    b = b[::-1]
    sum1 = str(int(a) + int(b))
    ans = int(sum1[::-1])
    print(ans)
'''
'''
#FCTRL2(spoj)
import math
for _ in range(int(input())):
    a = int(input())
    print(math.factorial(a))
'''
'''
#PALIN(spoj)
def palin(i):
    a1=i[::-1]
    if a1==i:
        print(a1)
    else:
        pass
for _ in range(int(input())):
    a=int(input())
    for i in range(a,100000000):
        i=str(i)
        print(palin(i))
'''
'''
#LASTDIG(spoj)
for _ in range(int(input())):
    a,b = map(int,input().split())
    ans = str(pow(a,b))[-1]
    print(ans)
'''
'''
#MSV(codechef, OCT 19B)
for _ in range(int(input())):
    a = int(input())
    l1 = list(map(int,input().split()))
    if len(l1)<=1:
        print(0)
    else:
        l=[]
        for i in range(1,len(l1)):
            print(l1[i])
            count=0
            for j in range(0,l1.index(l1[i])):
                print(l1[j])
                if l1[j]%l1[i] == 0:
                    count += 1
                print(count)
            l.append(count)
            print(l)
        ans = max(l)
        print(ans)
'''
'''
#vpropel(caesar cipher)
alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str1 = list(input())
d = int(input())
for i in range(len(str1)):
    str1[i] = alp[alp.index(str1[i])+d]
for i in str1:
    print(i,end='')
'''
'''
#vpropel(Multiples Of a number)
number = int(input())
range_=int(input())
l=[]
for i in range(1,range_+1):
    l.append(number*i)
for i in l:
    print(i,end=' ')
'''
'''
#vpropel(Pattern 2)
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
'''
'''
#vpropel(Number of Words)
pages = int(input())
print(pages*18*15)
'''
'''
#vpropel(Age in Seconds)
days = int(input())
print(days*24*60*60)
'''
'''
#vpropel(Arithmetic Expression)
number = int(input())
l = []
for i in range(1,number+1):
    l.append(pow(i,2))
print(sum(l)-number)
'''
'''
#vpropel(Digit Factors in a Number)
a = int(input())
b = str(a)
l = []
m = []

for i in b:
    if i != '0':
        l.append(i)

for i in range(len(l)):
    l[i] = int(l[i])

for i in l:
    if a % i == 0:
        m.append(i)
if all (a % i != 0 for i in l)==True:
    print('No factors')
else:
    m = m[::-1]
    print(*m)
'''
'''
#vpropel(Arrangement of Plants)
d = {}
for _ in range(int(input())):
    ID = (input())
    h = int(input())
    d[ID] = h
list1 = (sorted(d.items(), key=lambda x: x[1]))
list2 = []
for i in list1:
    list2.append(i[0])
for i in range(len(list2)):
    list2[i] = int(list2[i])
print(list2)
'''
'''
#vpropel (Game of Dragons)
strength,n = map(int,input().split())
dragons = sorted([list(map(int,input().split()))for i in range(n)],key=lambda x:x[0])
for dragon in dragons:
    if dragon[0] >= strength:
        print('NO')
        break
    else: strength += dragon[1]
else: print('YES')
'''
'''
#Time Conversion (vpropel)
time = input()
if time == '12:00:00AM':
    print('00:00:00')
elif time == '12:00:00PM':
    print('12:00:00')
else:
    time1 = list(time)
    if 'A' in time1:
        del time1[len(time1)-2:len(time1)]
        for i in time1:
            print(i,end='')
    else:
        del time1[len(time1)-2:len(time1)    ]
        a = int("".join(time1[0:2]))
        b = a+12
        del time1[0:2]
        time1.insert(0,b)
        for i in time1:
            print(i,end='')
'''
''' 
#Password Check (vpropel)
import re
pwd = input()
if len(pwd) >= 8:
    if re.match("^[a-zA-Z][a-zA-Z]+[0-9]*[!@#$%^&*()-]+",pwd):
        print('Valid')
    else:
        print('Invalid')
else:
    print('Invalid')
'''
'''
#Creating Unique List and Searching (vpropel)
l1=[]
for _ in range(int(input())):
    std = int(input())  
    l1.append(std)   
r = int(input())

for i in l1:
    if l1.count(i)>1:
        l1.remove(i)
print(l1)
if r in l1:
    print('Found')
else:
    print('Not Found')
'''
'''
#DF-2 (vpropel)
n = input()
n3 = int(n)
l=[]
l1=[]
n1 = list(n)
while '0' in n1:
    n1.remove('0')
for i in n1:
    l1.append(i)
n2 = str("".join(l1))   
for i in n2:
    i = int(i)
    n2 = int(n2)
    if n2%i == 0:
        l.append(i)
for i in range(len(l1)):
    l1[i] = int(l1[i])
if all(n3%i != 0 for i in l1)==True:
    print('No factors')
else:
    l = l[::-1]
    l = str(l)
    print (l[1:len(l)-1])    
'''
'''
#SAKTAN(codechef, 19OCTB)
import math
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    l1 = []
    l2 =[]
    for i in range(a):
        l1.append(0)
        l2.append(l1)
    for i in range(c):
        x,y  = map(int,input().split())
        l2[x][y] = 1
        l2[x-1][y-1] = 1
    print(l2)
       
'''

'''
#Number inversions(vpropel)
n = list(map(int,input()))
for i in range(len(n)):
    n[i] == int(n[i])
    if n[0] != 9 and n[i] >= 5 :
        n[i] == 9-n[i]
print(n)
ans = int("".join(n))
print(ans)        
'''
'''
#GHOME (codechef)
import math
m,n = map(int,input().split())
ans = (math.ceil((m*n)/2))
print(ans)
'''
'''
#MSNSADM1 (codechef)
for _ in range(int(input())):
    l = []
    N = int(input())
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    for i in range(len(list1)):
        l.append(list1[i]*20 - list2[i]*10)
    for i in range(len(l)):
        if l[i] < 0:
            l[i] = 0
        else:
            pass
    print(max(l))
'''
'''
#RHSAT (codechef)
q = int(input())
for _ in range(q):
    l1 = []
    l2 = []
    a = int(input())
    b = int(input())
    for i in range(1,a+1):
        l1.append(str(i))
    for i in range(1,b+1):
        l2.append(str(i))
    s1 = str(''.join(l1))
    s2 = str(''.join(l2))
    ans = int((s1[a-1])+(s2[b-1]))
    print(ans)
'''
'''
#RHSAT (codechef)
q = int(input())
l1 = []
for _ in range(q):
    a = int(input())
    l1.append(a)
l2 = []
for i in l1:
    l3 = []
    for j in range(1,i+1):
        l3.append(str(j))
    l2.append(l3)
l4 = []
for i in l2:
    s1 = str(''.join((i)))
    l4.append(s1)
l5 = []
for i in range(len(l4)):
    l5.append(l4[i][l1[i]-1])
for i in range(len(l5)):
    l5[i] = int(l5[i])
print(sum(l5))
'''
'''
#RPH001
for _ in range(int(input())):
    a,b = input().split()
    ans = int(str(int(a[::-1]) + int(b[::-1]))[::-1])
    print(ans)
'''
'''
#vpropel (Rotating Words)
word = input()
print(word)
l2=[]
for i in range(len(word)):
    word1 = word[-1] + word[:-1:]
    word = word1
    l2.append(word1)
print(len(set(l2)))
'''
'''
#MINEAT (codechef)
for _ in range(int(input())):
    l1 = []
    N,H = map(int,input().split())
    ban = list(map(int,input().split()))
'''
'''
#MKFR77 (codechef)
N,X = map(int,input().split())
can = list(map(int,input().split()))
c = 0
for i in can:
    if i>X: c+=1
    else: pass
print(c)
'''
'''
#DEVUGRAP (codechef)
for _ in range(int(input())):
    N,K = map(int.input().split())
    grp = list(map(int,input().split()))
'''
'''
#QUALPREL (codechef)
for _ in range(int(input())):
    N,K  = map(int,input().split())
    list1 = list(map(int,input().split()))
    list1.sort()
    list1 = list1[::-1]
    kth = list1[K-1]
    c=0
    for i in list1:
        if i >= kth:
            c+=1
    print(c)
'''
'''
#AVGAGE (codechef, extcontest)
for _ in range(int(input())):
    a,b,c = map(int,input().split())
'''

# AMSGAME1 (codechef)
'''
for _ in range(int(input())):
    N = int(input())
    list1 = list(map(int,input().split()))
    def find_gcd(x,y):
        while(y):
            x,y = y,x%y
        return x
    num1 = list1[0]
    num2 = list1[1]
    gcd = find_gcd(num1,num2)
    for i in range(2,len(list1)):
        gcd = find_gcd(gcd,list1[i])
    print(gcd)
'''
'''   
#FLOW016 (codechef)
import math
for _ in range(int(input())):
    a , b = map(int,input().split())
    l = []
    l.append(math.gcd(a,b))
    l.append(int((a*b)/math.gcd(a,b)))
    for i in l:
        print(i,end=' ')
'''
'''
#CANDY123(codechef)
for _ in range(int(input())):
    A,B = map(int,input().split())
    limak = []
    bob = []
    for i in range(1,1011,2):
        limak.append(i)
    for i in range(2,1010,2):
        bob.append(i)
'''
'''
#TWOVSTEN (codechef)
for _ in range(int(input())):
    x = int(input())
    if x%5 == 0:
        c=0
        while x%10:
            x *= 2
            c+=1
        print(c)
    else:
        print(-1)
'''
'''
#FLOW017 (codechef)
for _ in range(int(input())):
    list1 = list(map(int,input().split()))
    print(sorted(list1)[1])
'''
'''
#TLG(codechef)
l = []
l1 = []
temp1 = 0
temp2 = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    temp1 += a
    temp2 += b
    l.append(temp1 - temp2)
    l1.append(abs(temp1 - temp2))
if max(l) < max(l1):
    print(2, max(l1))
else:
    print(1, max(l))
'''
'''
#Picnic Groups (vpropel)
import math
nog = int(input())
sog = list(map(int,input().split()))
c = 0
while 4 in sog:
    c+=1
    sog.remove(4)
x = min(sog.count(3),sog.count(1))
c += x
for _ in range(x):
    sog.remove(3)
    sog.remove(1)
count += sog.count(3)
while 3 in sog: 
    sog.remove(3)
c += math.ceil(sum(sog)/4)
print(c)
'''
'''
#XORNEY (codechef) 
for _ in range(int(input())):
    L,R = map(int,input().split())
    m = 0
    if R-L == 0:
        b = R
        if b%2 == 0: print('Even')
        else: print('Odd')
    elif R-L == 1:
        b = R^L
        if b%2 == 0: print('Even')
        else: print('Odd')
    else:
        for i in range(L,R+1):
            b = m^i
            m = m^i
        if b%2 == 0: print('Even')
        else: print('Odd')
'''
'''
#RECIPE(codechef)
import math
for _ in range(int(input())):
    list1 = list(map(int,input().split()))
    list1.remove(list1[0])
    a = math.gcd(list1[0],list1[1])
    for i in range(2,len(list1)):
        b = math.gcd(a,list1[i])
        a = math.gcd(a,list1[i])
    for i in range(len(list1)):
        list1[i] = int(list1[i]/a)
    for i in list1:
        print(i,end=' ')      
'''
'''  
#MSNG(codechef)
for _ in range(int(input())):
    base = []
    n = []
    for _ in range(int(input())):
        b , N = input().split()
        base.append(b)
        n.append(N)
    for i in base:
        if i!='-1':
            a=i
    idx = base.index(a)
    n[idx] = n[idx][::-1]
    c = 0
    n[idx] = list(n[idx])
    for i in range(len(n[idx])):
        n[idx][i] = int(n[idx][i])
        d = n[idx][i]*(int(a)**i) + c
        c = n[idx][i]*(int(a)**i)
    print(d)
'''
''' 
#AMR15A (codechef)
a = int(input())
list1 = list(map(int,input().split()))
l1 = []
l2 = []
for i in list1:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
if len(l1)==len(l2):
    print('NOT READY')
else:
    if len(l1)>len(l2):
        print('READY FOR BATTLE')
    else:
        print('NOT READY')
'''
'''
#AVN006(codechef)
for _ in range(int(input())):
    list1 = list(map(int,input().split()))
    a = list1[0]
    del list1[0]
    list2 = []
    for i in range(len(list1)):
        list2.append(a-list1[i])
    print(list1[list2.index(min(list2))])
'''
'''
#SECPASS(codechef)
for _ in range(int(input())):
    l = []
    lt = int(input())
    s = input()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            l.append(s[i:j])
    l = sorted(l,key=len)[::-1]
    c = 0
    n = l[-1]
    l2 = []
    for i in l:
        curr = l.count(i)
        if curr > c:
            c = curr
            n = i
            l2.append(i)
    l3 = []
    for i in l2:
        l3.append(l.count(i))
    print(l2[l3.index(max(l3))])
'''
'''
#Fibanocci Increment Mixed String (vpropel)
s1,s2,n = input(),input(),int(input())
for _ in range(n-2):
    s3 = [chr(ord('a')+(ord(i)-ord('a')+1)%26)for i in [s1[j] if j%2==0 else s2[j] for j in range(len(s1))]]
    s1,s2 = s2,s3
print(*s3,sep='')
'''
'''
#FLOW008 (codechef)
for _ in range(int(input())):
    N = int(input())
    if N > 10: print('What an obedient servant you are!')
    else: print(-1)
'''
'''
#REMISS (codechef)
for _ in range(int(input())):
    l = list(map(int,input().split()))
    print(sorted(l)[1],sorted(l)[1]+sorted(l)[0])
'''
'''
#HEADBOB(codechef)
for _ in range(int(input())):
    a = int(input())
    b = input()
    if all(i == 'N' for i in b)==True: print('NOT SURE')
    elif 'Y' in b: print('NOT INDIAN')
    elif 'Y' not in b: print('INDIAN')
    else: pass
'''
'''
#FLOW014 (codechef) 
for _ in range(int(input())):
    h,c,t = map(float,input().split())
    if h > 50 and c < 0.7 and t > 5600: print(10)
    elif h > 50 and c < 0.7 and h < 5600: print(9)
    elif h < 50 and c < 0.7 and t > 5600: print(8)
    elif h > 50 and c > 0.7 and t > 5600: print(7)
    elif (h > 50 and c > 0.7 and t < 5600) or (h < 50 and c < 0.7 and t < 5600) or (h < 50 and c > 0.7 and t > 5600): print(6)
    elif h < 50 and c > 0.7 and t < 5600: print(5)
    else: pass
'''
'''
#FLOW011 (codechef)
for _ in range(int(input())):
    s = int(input())
    if s < 1500:
        hra = 0.1 * s
        da = 0.9 * s
        print(s + hra + da)
    else:
        hra = 500
        da = 0.98 *s
        print(s + hra + da)
'''
'''
#GDOG(codechef)
for _ in range(int(input())):
    N,K = map(int,input().split())
    print(N%K)
'''
'''
#CEQUAL (codechef)
f=0
from itertools import combinations
for _ in range(int(input())):
    a = int(input())
    list1 = list(map(int,input().split()))
    b = list(combinations(list1,2))
    for i in b:
        print(i)
        if i[0]==i[1]:
            f=1
            break
        else:
            f=0
    if f==1: print('YES')
    elif f==0: print('NO')
    else: pass
'''
'''
#MAX2 (codechef) (TLE)
l = []
X = int(input())
N = int(input())  
binary1 = N 
decimal, i, n = 0, 0, 0
while(N != 0): 
    dec = N % 10
    decimal = decimal + dec * pow(2, i) 
    N = N//10
    i += 1 
i=1
while decimal%(2**i) == 0:
    l.append(i)
    i += 1
print (max(l))
#correct NO TLE
l = []
X = int(input())
N = input()
b = list(N[::-1])
i = 0
l1 = []
for i in range(len(b)):
    b[i] = int(b[i])
    l1.append(b[i]*(2**(i)))
i=1
while sum(l1)%(2**i) == 0:
    l.append(i)
    i += 1
print (max(l))
'''
'''
#AVG (codechef)
for _ in range(int(input())):
    n,k,v = map(int,input().split())
    l1 = list(map(int,input().split()))
    sum1 = v*(n+k)
    sum2 = sum(l1)
    if sum1 > sum2:
        diff = sum1-sum2
        if diff%k == 0:
            ans = int(diff/k)
            print(ans)
        else:
            print(-1)
    else: print(-1)
'''
'''
#ATTND (codechef)
for _ in range(int(input())):
    l1 = []
    l2 = []
    for _ in range(int(input())):
        a,b = map(str,input().split())
        l1.append(a)
        l2.append(b)
    l3 = []
    for i in range(len(l1)):
        if l1.count(l1[i])>1:
            l3.append(l2[i])
    l4 = []
    for i in l3:
        if i not in l2:
            l4.append(i)
    print(l1)
    print(l2)
    print(l4)        
'''
'''
#RPD (codechef)
from itertools import combinations
for _ in range(int(input())):
    a = int(input())
    l1 = list(map(int,input().split()))
    b = list(combinations(l1,2))
    l2 = []
    l3 = []
    for i in b:
        l2.append(i[0]*i[1])
    for i in range(len(l2)):
        l2[i] = str(l2[i])
    for i in l2:
        i = list(i)
        l4 = []
        for j in range(len(i)):
            i[j] = int(i[j])
            l4.append(i[j])
        l3.append(sum(l4))
    print(max(l3))            
'''
'''
#PLAYSTR (codechef)
for _ in range(int(input())):
    a = int(input())
    S = list(input())
    R = list(input())
    c = S.count('1')
    d = R.count('1')
    if c == d:
        if len(S) == len(R): print('YES')
        else: print('NO')
    else: print('NO')
'''
'''
#CHFTIRED (codechef)
for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(1000000000):
        if a > b:
            a = a + i-1
            b = b + i
            if a == b:
                f = 0
                break
            else: f = 1
        elif a < b:
            a = a + i
            b = b + i - 1
            if a == b:
                f = 0
                break
            else: f = 1
    if f == 0:
        print('YES')
    elif f == 1:
        print('NO')
    else: pass
'''
'''
#PLAYPIAN (codechef)
for _ in range(int(input())):
    f = 1
    s = input()
    for i in range(1,len(s),2):
        if s[i-1] == s[i]:
            f = 0
            break
        else:
            f = 1
    if f == 0:
        print('no')
    else:
        print('yes')
'''
'''
#SUMAGCD (codechef)
import math
for _ in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    l1 = []
    l2 = []
    for i in lst:
        if i%2 == 0:
            l1.append(i)
        else: l2.append(i)
    if len(l1) < 2:
        l1.append(l1[0])
    elif len(l2) < 2:
        l2.append(l2[0])
    else: 
        pass
    a = l1[0]
    e = l2[0]
    for i in range(1,len(l1)):
        gcd1 = math.gcd(a,l1[i])
        a = math.gcd(a,l1[i])
    print(l1)
    print(gcd1)
    for i in range(1,len(l2)):
        gcd2 = math.gcd(e,l2[i])
        e = math.gcd(e,l2[i])
    print(l2)
    print(gcd2)
    print(gcd1 + gcd2)
'''
'''
#AREAPERI (codechef)
L = int(input())
B = int(input())
Area = L * B
Peri = 2 * (L + B)
if Area > Peri:
    print('Area')
    print(Area)
elif Peri > Area:
    print('Peri')
    print(Peri)
else:
    print('Eq')
'''
'''
#KCON (codechef)
for _ in range(int(input())):
    N,K = map(int,input().split())
    list1 = list(map(int,input().split()))
    list2 = []
    for i in range(K):
        list2.append(list1)
    list3 = []
    for i in list2:
        for j in i:
            list3.append(j)
    list4 = []
    for i in range(len(list3)):
        for j in range(i+1,len(list3)+1):
            sub = list3[i:j]
            list4.append(sub)
    list5 = []
    for i in list4:
        list5.append(sum(i))
    print(max(list5))
'''
'''
#CV (codechef)
for _ in range(int(input())):
    a = int(input())
    s = list(input())
    c = 0
    for i in range(1,len(s)):
        if s[i-1] in 'bcdfghjklmnpqrstvwxyz' and s[i] in 'aeiou':
            c+=1
    print(c)
'''
'''
#JKR1 (codecehef)
for _ in range(int(input())):
    a = int(input())
    l1 = list(map(str,input().split()))
    b = l1[-1][::-1]
    l1.remove(l1[-1])
    l1.insert(0,b)
    for i in range(3,len(l1),2):
        prev = l1[i-1]
        l1[i-1] = l1[i]
        l1[i] = prev
    for i in l1:
        print(i, end = ' ')
'''
'''
#JKR6 (codechef)
l1 = []
l2 = []
a,b = input().split()
for i in range(len(b)):
    for j in range(i+1,len(b)+1):
        sub = b[i:j]
        l1.append(sub)
print (l1)
for i in l1:
    if i == i[::-1]:
        l2.append(len(i))
print(l2)
print(max(l2))
'''
'''
#LECANDY (codechef)
for _ in range(int(input())):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))
    print('Yes' if sum(lst) <= K else 'No')
'''
'''
#RESQ (codechef) (wrong approach)
def primeFactors(n):
    import math
    l1 = []
    while n%2 == 0:
        l1.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            l1.append(int(i))
            n = n / i
    if n > 2:
        l1.append(n)
    return l1
for _ in range(int(input())):
    n = int(input())
    if n == 1: print(0)
    else:
        lst = primeFactors(n)
        i = 0
        x = 1
        for i in range(len(lst)-1):
            x *= lst[i]
            i += 1
        ans = int(abs(x - lst[-1]))
        print(ans)
'''
'''
#TACHSTCK (codechef)
from itertools import combinations
N,D = map(int,input().split())
l1 = []
for _ in range(N):
    l1.append(int(input()))
l2 = list(combinations(l1,2))
c = 0
for i in l2:
    if int(abs(i[0]-i[1])) == D:
        c += 1
print(c)
#or
n,d=map(int,input().split())
l=list()
for i in range(n):
    l.append(int(input()))
count=0
k=0
l.sort()
while k<n-1:
    if(l[k+1] -l[k])<=d:
        count+=1
        k+=1
    k+=1
print(count)
'''
'''
#PCJ18B (codechef)
for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in range(1,n + 1,2):
        k = n - i + 1
        c += (k * k)
    print(c)
'''
'''
#LONGSEQ (codechef)
for _ in range(int(input())):
    n = list(input())
    if n.count('0') == 1 or n.count('1') == 1: print('Yes')
    else: print('No')
'''
'''
#MISSP (codechef)
for _ in range(int(input())):
    l=[]
    for i in range(int(input())):
        a=int(input())
        l.append(a)
    l.sort()
    if len(l) % 2 != 0:
        l.append(0)
    else:
        pass
    l1 = []
    for i in range(1,len(l),2):
        l1.append([l[i-1],l[i]])
    for i in l1:
        if i[0] != i[1]:
            print(i[0])
            break
'''
'''
#CHEFINSQ (codechef) (30/100)
from itertools import combinations
for _ in range(int(input())):
    N,K = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(combinations(l1,K))
    l3 = []
    for i in l2:
        l3.append(sum(i))
    c = 0
    for i in l2:
        if sum(i) == min(l3):
            c += 1
    print(c)
'''
'''   
#GDSUB (codechef) (TLE)
from itertools import combinations
N,K = map(int,input().split())
lst = list(map(int,input().split()))
l1 = []
for i in range(2,K+1):
    l2 = (list(combinations(lst,i)))
    for i in l2:
        l1.append(i)
c = 0
for i in l1:
    if len(set(i)) == len(i):
        c += 1
print(c + len(lst) + 1)
'''
'''
#NBSUM (codechef) (100/100, divy)
for _ in range(int(input())):
    n = int(input())
    print(int((n * (n + 1)) / 2) - 4 * (int(((n // 2) * ((n // 2) + 1)) / 2)))
'''
'''
#COINFLIP (codechef)
for _ in range(int(input())):
    for G in range(int(input())):
        i,n,q = map(int,input().split())
        
        if(n%2==0):
            print(n//2)
            
        else:
            if (i==1):
                
                if (q==1):
                    print(n//2)
                else:
                    print(n//2 + 1)
                    
            else:
                
                if(q==1):
                    print(n//2 + 1)
                else:
                    print(n//2)
#or
for _ in range(int(input())):
    for _ in range(int(input())):
        lst = list(map(int,input().split()))
        if lst[1] % 2 == 0:
            print(int(lst[1] // 2))
        else:
            if lst[0] == 1:
                if lst[2] == 1: print(int((lst[1]) // 2))
                else: print(int(((lst[1]) // 2) + 1))
            else:
                if lst[2] == 1: print(int(((lst[1]) // 2) + 1))
                else: print(int((lst[1]) // 2))
'''
'''
#KQM16B
s = list(input())
c = 0
d = 0
s1 = s[::-1]
for i in range(len(s)):
    if s == s[::-1]:
        pass
    else:
        s.remove(s[0])
        c += 1
for i in range(len(s1)):
    if s1 == s1[::-1]:
        pass
    else:
        s1.remove(s1[0])
        d += 1
print(min(c,d))
'''
'''
#KQM16A (codechef)
from itertools import combinations
lst = []
a = int(input())
n = list(map(int,input().split()))
for i in range(1,len(n)+1):
    lst.append(list(combinations(n,i)))
c = 0 
for i in lst:
    for j in i:
        j = list(j)
        if j == sorted(j) and len(j) == len(set(j)):
            c += 1
print(c)


from itertools import combinations
for _ in range(int(input())):
    l1 = []
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    for _ in range(k):
        a = int(input())
        l1.append(a)
    for i in l1:
        c = 0
        l2 = list(combinations(lst,i))
        print(list(set(l2)))
        for j in list(set(l2)):
            j = list(j)
            if len(j) == len(set(j)):
                c += 1
        print(c)
'''
'''
#SPELLBOB (codechef)
for _ in range(int(input())):
    lst1 = [i for i in input()]
    lst2 = [i for i in input()]
    for i in range(len(lst1)):
        if ((lst1[i] in 'bob') and (lst2[i] in 'bob')) and lst1[i] != lst2[i]:
            f = 0
            break
        else:
            f = 1
    if f == 0:
        print('no')
    else:
        print('yes')
'''
'''
#JOHNY (codechef)
for _ in range(int(input())):
    N = int(input())
    lst1 = list(map(int,input().split()))
    K = int(input())
    value = lst1[K-1]
    lst1.sort()
    print((lst1.index(value))+1)
'''
'''
#BINARY (codechef) (WA)
for _ in range(int(input())):
    l,a = map(int,input().split())
    lst1 = list(map(int,input().split()))
    for i in range(a):
        v = lst1[-1]
        lst1.remove(v)
        lst1.insert(0,v)
        for i in range(1,len(lst1),2):
            if lst1[i-1] == lst1[i]:
                break
            else:
                pass
    for i in lst1: print(i, end = ' ')
'''
'''
#PCJ18A (codechef)
for _ in range(int(input())):
    a,b = map(int,input().split())
    ls1 = list(map(int,input().split()))
    if all (i < b for i in ls1) == True: print('NO')
    else: print('YES')
'''
'''
#BUYING 2 (codechef)
for _ in range(int(input())):
    a,b = map(int,input().split())
    lst1 = list(map(int,input().split()))
    tot = sum(lst1)
    lst1.sort()
    val = lst1[0]
    lst2 = lst1
    lst2.remove(val)
    tot1 = sum(lst1)
    if tot%b != 0 and tot1 // b == tot // b:
        print(-1)
    else:
        print(tot // b)
'''
'''
#EXUNA (codechef)
for _ in range(int(input())):
    a = int(input())
    l = list(map(int,input().split()))
    print (sorted(l)[0])
'''
'''
#GTXOR (codechef)
for _ in range(int(input())):
    x = int(input())
    c = 0
    for i in range(1,x):
        if i ^ x > x:
            c += 1
    print(c)
'''
'''
#NAME2 (codehchef)
for _ in range(int(input())):
    a,b = map(str,input().split())
    if len(a) < len(b):
        f = 0
        for i in a:
            if i in b:
                f = 0
            else:
                f = 1
        if f == 0:
            print('YES')
        else: print('NO')
    elif len(a) > len(b):
        f = 0
        for i in b:
            if i in a:
                f = 0
            else:
                f = 1
        if f == 0: print('YES')
        else: print('NO')
    else:
        if a == b:
            print('YES')
        else:
            print('NO')
            
'''
'''
#GCDQ (codechef)
def gcd(a,b):
   if b == 0:
       return a
   else:
       return gcd(b,a%b)
for _ in range(int(input())):
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    for _ in range(Q):
        L,R = map(int,input().split())
        A1 = []
        A2 = []
        for i in range(L-1,R):
            A2.append(A[i])
        for i in A:
            if i not in A2:
                A1.append(i)
        f = A1[0]
        for i in A1:
            a = gcd(f,i)
            c = gcd(a,i)
        print(c)
'''
'''
#SETH002 (codechef)
for _ in range(int(input())):
    L = []
    A,B,C = map(int,input().split())
    for i in range(A):
        L.append(1)
    for i in range(B):
        L.append(2)
    for i in range(C):
        L.append(3)
sum1 = 3*L.count(3)
def partition(s):
    answer = set()
    answer.add((s, ))
    for x in range(1,s):
        for y in partition(s-x):
            answer.add(tuple(sorted((x,)+y)))
    return answer
if len(partition(sum1)) == 0:
    print('NO')
else:
    print('YES')
'''

'''               
#SETH0005 (codechef)
a,b = map(int,input().split())
if a >= 2*b or b >= 2*a:
    c = 0
    for i in range(100):
        c += i
        a += i
        b += i
        if a % b == 0 or b % a == 0:
            print(c)
            break
else:
    print(0)
'''
'''
#SETH0006 (codechef)
l,r = map(int,input().split())
L = []
for i in range(l,r+1):
    L.append(i)
for i in range(len(L)):
    L[i] = str(L[i])
    L[i] = list(L[i])
if all(len(i) != len(set(i)) for i in L) == True:
    print(-1)
else:
    for i in L:
        if len(i) == len(set(i)):
            a = int(str(''.join(i)))
            print(a)
            break
'''
'''
#SETH0004 (codechef)
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
L2 = []
L1 = []
v = arr[0]
colours = 0
for i in arr:
    if i % v == 0:
        L1.append(i)
    else:
        L2.append(i)
L2.append(L1)
print(len(L2))
'''
'''
#NOTINCOM (codechef)
for _ in range(int(input())):
    a, b = map(int, input().split())
    l = [[int(i) for i in input().split()], [int(i) for i in input().split()]]
    res = list(set.intersection(*map(set, l)))
    print(len(res))
'''
'''
#DIVIDING
N = int(input())
A = sum(list(map(int,input().split())))
sum1 = (N * (N + 1)) / 2
print('YES' if sum1 == A else 'NO')
'''
'''
#CHEFAPAR (codechef) (WA)
for _ in range(int(input())):
    a = int(input())
    l1 = list(map(int,input().split()))
    if l1.count(1) == len(l1):
        print(0)
    else:
        print((1000 * l1.count(0)) + (100 * len(l1)))
'''
'''
#CHIN000 (codechef)
def SUM(A):
    return sum([i for i in range(A+1)])
for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(a):
        sum2 = SUM(b)
        b = SUM(b)
    print(sum2)
'''
'''
#DISTCHOC (codechef)]a = int(input())
lst = list(map(int,input().split()))
l = sorted(lst)
c = 0
for i in l:
    for j in range(0,l.index(i)):
        c += l[j]
print(c)

# OR 
L = []
a = int(input())
lst = list(map(int,input().split()))
l = sorted(lst)
l.remove(l[-1])
c = 0
for i in range(len(l)):
    for j in range(i+1,len(l)+1):
        sub = l[i:j]
        L.append(sub)
sum1 = 0
for i in L[0:len(l)]:
    for j in i:
        sum1 += j        
print(sum1)

#OR
L = []
a = int(input())
lst = list(map(int,input().split()))
lst.sorted()
lst.remove(-1)
sum2 = 0
for i in range(len(lst)):
    sum1 = sum(lst)
    lst.remove(lst[-1])
    L.append(sum1)
print(sum(L))
'''
'''
#STAIRCASE (hackerrank)
n = int(input())
def staircase(num_stairs):
    n = num_stairs - 2
    for stairs in range(1, num_stairs):
        print(' ' * n, '#' * stairs)
        n -= 1
    return '#' * num_stairs
print(staircase(n))
'''
'''
#mini-max-probem (hackerank)
lst = sorted(list(map(int,input().split())))
print (sum((lst)[0:len(lst)-1]) , sum((lst)[1:len(lst)]) , end = ' ')
'''
'''
#birthday-cake-candles (hackerrank)
a = int(input())
lst = list(map(int,input().split()))
print(lst.count(max(lst)))
'''
'''
#diagonal difference (hackerrank)
L = []
L1 = []
L2 = []
n = int(input())
for i in range(n):
    lst  = list(map(int,input().split()))
    L.append(lst)
for i in range(len(L)):
    L1.append(L[i][i])
for i in range(len(L)-1,-1,-1):
    L2.append(L[len(L)-i-1][i])     
print(abs(sum(L1) - sum(L2)))
'''
'''
#grading (hackerrank)
for _ in range(int(input())):
    a = int(input())
    if a  < 38:
        print(a)

    elif abs(a - 5 * ((a // 5) + 1)) < 3:
        print(5 * ((a // 5) + 1))

    else:
        print(a)
'''
'''
#breaking the records (hackerrank)
a = int(input())
lst = list(map(int,input().split()))
br = 0
nt_br = 0
for i in range(1,len(l)):
    if all(l[i] > l[i-1] for j in range(0,i+1)) == True:
        br += 1
    elif 
        nt_br += 1
print(br,nt_br,end=' ')
'''
'''
from itertools import combinations 
a,b = map(int,input().split())
lst = list(map(int,input().split()))
l1 = list(combinations(lst,2))
c = 0
for i in l1:
    if sum(i) % b == 0: c += 1
print(c)

#the hurdle race (hackerrank)
a,b = map(int,input().split())
lst = list(map(int,input().split()))
print(0 if max(lst) <= b else max(lst) - b)
'''
'''
l = []
s = list(input())
ss = list(input())
c = 0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub = s[i:j]
        l.append(sub)
c = 0
for i in l:
    if i  == ss:
        c += 1
print(c)
'''
'''
#compare the triplets (hackerrank)
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
b = 0
a = 0
for i in range(len(lst1)):
    if lst1[i] > lst2[i]:
        b += 1
    elif lst1[i] < lst2[i]:
        a += 1
    else:
        pass
print(b,a,end =' ')
'''
'''
#bon-appetit (hakerrank)
n,k = map(int,input().split())
lst1 = list(map(int,input().split()))
b = int(input())
lst1.remove(lst1[k])
sum1 = sum(lst1)
bac = sum1 // 2
if bac == b:
    print('Bon Appetit')
else:
    print(abs(b - bac))
'''
'''
# divisible sum pairs
from itertools import combinations
n,k = map(int,input().split())
lst1 = list(map(int,input().split()))
lst2 = list(combinations(lst1,2))
c = 0
for i in lst2:
    if sum(i) % k == 0:
        c += 1
print(c)
'''
'''
#sock-merchant (hackerrank)
n = int(input())
lst1 = list(map(int,input().split()))
set1 = set(lst1)
l1 = []
for i in set1:
    if lst1.count(i) > 1:
        l1.append(lst1.count(i))
print(sum(l1) // 2)
'''
'''
#vpropel BAT Deficient Numbers
n = int(input())
l1 = []
for i in range(2,n):
    if n % i == 0:
        l1.append(i)
if sum(l1) < n:
    print('Deficient')
else:
    print('Not deficient')
'''
'''
#vpropel BAT Palindrome or Symmentry
for _ in range(int(input())):

    n = list(input())
    n = [n[i].lower() for i in range(len(n))]
    if len(n) % 2 != 0:
        n.remove(n[len(n)//2])
    else:
        pass
    if len(set(n)) == 1:
        print('Both property')
    else:
        if n[0:len(n)//2] == n[len(n)//2:len(n)]:
            print('Symmetry')
        elif n[0:len(n)//2] == n[len(n)//2:len(n)][::-1]:
            print('Palindrome')
        else:
            print('No property')
'''
'''
#vpropel BAT Pangram1
l1 = [i for i in 'abcdefghijklmnopqrstuvwxyz']
l2 = []
n = input()
for i in n:
    if i != ' ':
        l2.append(i.lower())
l2 = sorted(list(set(l2)))
if l1 == l2:
    print('Pangram')
else:
    print('Not pangram')
'''
'''
#vpropel BAT Vowelgram
l1 = []
n = input()
for i in n:
    if i != ' ':
        l1.append(i.lower())
if all(l1.count(i) == 1 for i in 'aeiou') == True:
    print('Vowelgram')
else:
    print('Not vowelgram')
'''
'''
#vpropel BAT 
l1 = []
n = input()
for i in n:
    if i != ' ':
        l1.append(i.lower())
if all(l1.count(i) >= 1 for i in 'aeiou') == True:
    print('Vowgram')
else:
    print('Not vowgram')
'''
'''
#designer pdf problem (hackerrank)
l1 = list(map(int,input().split()))
s = input()
l2 = [i for i in 'abcdefghijklmnopqrstuvwxyz']
l3 = [l2.index(i) for i in s]
print(max(l3) * len(s))
'''
'''

#vpropel BAT Identify machines in same local network
l1,l2,l3 = [],[],[]
n = int(input()) 
for _ in range((n * (n + 1)) // 2):
    a = int(input())
    l1.append(a)
for i in range(1,n + 1):
    l2.append(l1[0:i])
    del l1[0:i]
for i in l2:
    l3.append(max(i))
print(sum(l3))
'''
'''
#google kickstart Book Reading
for z in range(int(input())):
    n,m,q = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    l3 = [i for i in range(1,n+1)]
    l4 = []
    for i in l3:
        if i not in l1:
            l4.append(i)
    # l4 contains untorned pages
    c = 0
    for i in l2:
        for j in l4:
            if j % i == 0:
                c += 1
    print(('Case' + ' ' + '#' + str(z+1) + ':'),c)
'''
'''
#find digits (hackerrank)
for _ in range(int(input())):
    n = int(input())
    n1 = list(str(n))
    while '0' in n1:
        n1.remove('0')
    else:
        pass
    c = 0
    for i in range(len(n1)):
        n1[i] = int(n1[i])
        if n % n1[i] == 0:
            c += 1
    print(c)
'''
'''
#CHEFSUM (codechef)
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int,input().split()))
    #l2 = [sum(l1[0:i]) + sum(l1[i-1:len(l1)]) for i in range(1,n + 1)]
    #print(l2.index(min(l2)) + 1)
    print (l1.index(min(l1)) + 1)
'''
'''
#Palindromic Number (codepark)
for _ in range(int(input())):
    n = input()
    print ('Yes' if n == n[::-1] else 'No')
'''
'''
#PRMDIV
def psum(x):
    l1 = []
    for i in range(2,x + 1):
        if all (i % j != 0 for j in range(2, i)) == True:
            l1.append(i)
    return l1
a = int(input())
print(psum(a))

from itertools import combinations
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int,input().split()))
    l2 = set(list(combinations(l1,2))) | set(list(combinations(l1[::-1],2)))
    print(l2)
    l3 = []
    for i in l2:
        if i[0] % i[1] == 0 or i[1] % i[0] == 0:
            l3.append(i)
    print(l3)
'''
'''
#INFY1908 (codechef)
for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(b):
        a += 1
        if a % 10 == 0:
            a = a - 10
        else:
            pass
    print(a)
'''
'''
#INFY1912 (codechef)
for _ in range(int(input())):
    l2 = []
    n,k  = map(int,input().split())
    for i in range(n):
        l3 = []
        for j in range(n):
            l3.append(0)
        l2.append(l3)
    for _ in range(k):
        r,c = map(int,input().split())
        l2[r-1][c-1] += l2[r-1][c-1] + 1
    for i in range(len(l2)):
        if 1 in l2[i]:
            for j in range(1,len(l2[i])):
                l2[i-1][j-1] += 1
    c = 0
    for i in range(len(l2)):
        for j in range(len(l2[i])):
            if l2[i][j] == 0:
                c += 1
    if c == 0:
        print('Impossible')
    else:
        print(c,n*n,end=' ')
'''
'''            
#MDL (codechef)
for _ in range(int(input())):
    a = int(input())
    l1 = list(map(int,input().split()))
    idx1 = l1.index(max(l1))
    idx2 = l1.index(min(l1))
    if idx1 > idx2:
        print(min(l1), max(l1))
    else:
        print(max(l1), min(l1))
'''
'''
#DOR (codechef)
import math
for _ in range(int(input())):
    n = int(input())
    nsr = list(str(n))[::-1]
    nsl = [int(i) for i in nsr]
    c = 0
    l1 = []
    for i in nsl:
        l1.append(i)
        c += 1
        if i > 0:
            break
    del l1[-1]
    l2 = [nsl[i] for i in range(c-1, len(nsl))]
    l3 = [str(i) for i in l2[::-1]]
    num = int(str(''.join(l3)))
    l4 = [float(i) for i in range(0,19)]
    if (math.log(num,2)) in l4 and c-1 >= (math.log(num,2)):
        print('Yes')
    else:
        print('No')
'''
'''
#DOR (codechef)
for _ in range(int(input())):
    l,r = map(int,input().split())
    print(r | (r-1))
'''
'''
#NPLQ19D (codechef)
for _ in range(int(input())):
    a = list(input())
    l1 = []
    for i in a:
        if i not in l1:
            l1.append(i)
    print(str(''.join(l1)))
'''
'''
#NPLQ19E (codechef)
import math
def fac(m,n):
    return (math.factorial(m) // (math.factorial(n) * (math.factorial(m-n))))
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0, 1)
    elif n == 2:
        print(1, 2)
    else:
        l1 = [fac(n, i) for i in range(1, n+1, 2)]
        l2 = [fac(n, i) for i in range(2, n+1, 2)]
        print(sum(l2) % 1000000007, sum(l1) % 1000000007)
'''
'''
#subsequence
def subs(str1,str2,m,n):
    j = 0
    i = 0
    while j < m and i < n:
        if str1[j] == str2[i]:
            j+=1
        i+=1
    return j == m
str2 = input()
str1 = input()
m = len(str1)
n = len(str2)
print("Yes" if subs(str1,str2,m,n) else "No")
'''
'''
#MULTQ3 (codechef)
n,q = map(int,input().split())
for _ in range(q):
    c,a,b = map(int,input().split())
    if c = 0:
        pass
    else:
        l1 = [0] * n
        for i in range(a,b+1):
            l1[i] += 1
'''
'''
#ERROR (codechef)
#TLE
def iss(s1,s2):
    m = len(s1)
    n = len(s2)
    for i in range(n-m+1):
        for j in range(m):
            if (s2[i + j] != s1[j]):
                break
        if j + 1 == m:
            return 1
    return -1
for _ in range(int(input())):
    s1 = '101'
    s2 = input()
    s3 = '010'
    res1 = iss(s1,s2)
    res2 = iss(s3,s2)
    if res1 == -1 and res2 == -1:
        print('Bad')
    else:
        print('Good')
#OR (AC)
for _ in range(int(input())):
    a = input()
    if a.find('101') > 0 or a.find('010') > 0:
        print('Good')
    else:
        print('Bad')
'''
'''
#vpropel (Smallest Divisble Number)
import math
n = int(input())
l1 = [i for i in range(2,n+1,2)]
a = l1[0]
for i in range(1,len(l1)):
    lcm = (a*l1[i]) // math.gcd(a,l1[i])
    a = (a*l1[i]) // math.gcd(a,l1[i])
print(lcm)
'''
'''
#vpropel(BAT) GMT to IST
l1 = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Monday']
day = input()
hrs = int(input())
mins = int(input())
if mins < 30:
    mins = mins + 30
else:
    mins = abs(60 - (mins + 30))
if hrs < 19:
    hrs = hrs + 5
else:
    hrs = abs(24 - (hrs + 5))
if (hrs + (60 // mins)) > 0 and  (hrs + (60 // mins)) > hrs:
    print(l1[l1.index(day) + 1])
    print(hrs)
    print(mins)
    
else:
    print(day)
    print(hrs)
    print(mins)
'''
'''
#RAINBOWA (codechef)
for _ in range(int(input())):
    arr1 = [i for i in range(1,8)]
    a = int(input())
    l1 = list(map(int,input().split()))
    ls = sorted(l1)
    if (ls[0] < 0 or ls[-1] > 7) and l1[0:len(l1)] not in arr1:
        print('No')
    else:
        if len(l1) % 2 != 0:
            l2 = l1[0:(len(l1)//2)]
            l3 = l1[len(l1)//2 + 1:len(l1)]
            if l2 == l3[::-1]:
                print('Yes')
            else:
                print('No')
        else:   
            l2 = l1[0:(len(l1)//2)-1]
            l3 = l1[len(l1)//2:len(l1)]
            if l2 == l3[::-1]:
                print('Yes')
            else:
                print('No')
'''
'''
#COPS (codechef)
for _ in range(int(input())):
    m,x,y = map(int(input().split()))
    l1 = list(map(int,input().split()))
'''
'''
#EGRANDR (codechef)
for _ in range(int(input())):
    a = int(input())
    l1 = list(map(int,input().split()))
    if 5 not in l1:
        print('No')
    elif 1 in l1 or 2 in l1:
        print('No')
    else:
        print('Yes' if sum(l1)//a >= 4 else 'No')
'''
'''
#FRK (codechef)
l1 = []
for _ in range(int(input())):
    a = input()
    l1.append(a)
b = 'chef'
l2 = []
for i in range(len(b)):
    for j in range(i+2, len(b)+1):
        sub = b[i:j]
        l2.append(sub)
c = 0
for i in l1:
    for j in l2:
        if i.find(j) != -1:
            c+=1
            break
print(c)
'''
'''
#CHEFA (codechef)
for _ in range(int(input())):
    a = int(input())
    b = sorted(list(map(int,input().split())))[::-1]
    s = 0
    for i in range(0,len(b),2):
        s += b[i]
    print(s)
'''
'''
#ABSNUM (codechef)
for _ in range(int(input())):
    a = int(input())
    print(abs(a))
'''
'''
#ALPHABET (codechef)
s = sorted(list(input()))
for _ in range(int(input())):
    a = sorted(list(set(input())))
    print('Yes' if s == a else 'No')
'''
'''
#DANOW (codchef)
n,q = map(int,input().split())
l1 = list(map(int,input().split())) 
l2 = list(map(int,input().split()))
for i in range(q):
    l,r = map(int,input().split())
    l3 = []
    for i in range(l-1,r):
        l3.append(l1[i] * l2[i])
    print(sum(l3))
'''
'''
#camelcase (hackerrank)
a = input()
c = 0
for i in a:
    if i.isupper() == True:
        c += 1
print(c + 1)
'''
'''
#pangrams (hackerrank)
l1 = [i for i in 'abcdefghijklmnopqrstuvwxyz']
l2 = []
n = input()
for i in n:
    if i != ' ':
        l2.append(i.lower())
l2 = sorted(list(set(l2)))
if l1 == l2:
    print('pangram')
else:
    print('not pangram')
'''
'''
#TOTR (codechef)
a,b = input().split()
a = int(a)
b = str(b)
l = [i for i in b]
l4 = [i for i in b.upper()]
l2 = [i for i in 'abcdefghijklmnopqrstuvwxyz']
l3 = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
for i in range(a):
    l1 = list(map(str,input().split('_')))
    for i in range(len(l1)):
        l1[i] = list(l1[i])

        for j in range(len(l1[i])):
            if l1[i][j] in l2:    
                idx = l2.index(l1[i][j])
                l1[i][j] = l[idx]
            elif l1[i][j] in l3:
                idx = l3.index(l1[i][j])
                l1[i][j] = l4[idx]
            else:
                pass
        l1[i] = str(''.join(l1[i]))
    print(str(' '.join(l1)))
'''
'''
#HHAL (codechef)
for _ in range(int(input())):
    s = input()
    print(1 if s == s[::-1] else 2)
'''
'''
#EMITL (codechef)
for _ in range(int(input())):
    s = input()
    if len(s) == 9:
        print('YES' if(s.count('L') >= 2 and s.count('T') >= 2 and s.count('I') >= 2 and s.count('M') >= 2 and s.count('E') >= 1) else 'NO')
    else:
        print('YES' if(s.count('L') >= 2 and s.count('T') >= 2 and s.count('I') >= 2 and s.count('M') >= 2 and s.count('E') >= 2) else 'NO')
'''
'''
#MAXDIFF (codechef)
for _ in range(int(input())):
    n, k = map(int, input().split())
    l1 = sorted(list(map(int, input().split())))
    print(max((abs(sum(l1[k:]) - sum(l1[:k]))), (abs(sum(l1[n-k:]) - sum(l1[:n-k])))))
'''
'''
#ZCO14001 (codechef)
n, h = map(int, input().split())
hts = list(map(int, input().split()))
moves = list(map(int, input().split()))
j = 0
s = 0
for i in range(len(moves)):
    if moves[i] == 0:
        break
    elif moves[i] == 1 and j != 0:
        j -= 1
    elif moves[i] == 2 and j != n - 1:
        j += 1
    elif moves[i] == 3 and s == 0 and hts[j] != 0:
        hts[j] -= 1
        s += 1
    elif moves[i] == 4 and s == 1 and hts[j] < h:
        s -= 1
        hts[j] += 1
    else:
        pass
print(*hts)
'''
'''
# ZCO13001 (codechef)
from itertools import combinations
n = int(input())
team = [i for i in range(1, n+1)]
st = list(map(int, input().split()))
l1 = list(combinations(team, 2))
l2 = [abs(st[team.index(i[0])] - st[team.index(i[1])]) for i in l1]
print(sum(l2))
'''
'''
#vpropel (Stock Market)
a, b = map(int, input().split())
q = int(input())
l1 = list(map(int, input().split()))
l2 = [a, b]
for i in range(2, max(l1)):
    l2.append(((4 * l2[i - 2]) + (3 * l2[i - 1])))
for i in l1:
    print(l2[i-1], end=' ')
'''
'''
#INVZVNT (codechef)
for _ in range(int(input())):
    n, q = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
'''
'''
#HIT (codechef)
for _ in range(int(input())):
    a = int(input())
    b = sorted(list(map(int, input().split())))
    if 
        if len(b) == 4:
            print(*(b[1:]))
        else:
            c = len(b)
            l1 = sorted([i for i in range(c, 0, -c//4)])
            l1.remove(l1[-1])
            l2 = [b[i] for i in l1]
            print(*l2)
    else:
        print(-1)

'''
'''
#INVYCNT (codechef) (tle)
for _ in range(int(input())):
    a,b = map(int, input().split())
    l1 = list(map(int, input().split())) * b
    c = 0
    for i in range(len(l1)):
        for j in range(i,len(l1)):
            if l1[i] > l1[j]: c += 1
    print(c)
'''
'''
#vpropel(Skipping Stones):
from itertools import combinations
for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(1)
        a.append(2)
    l = []
    for i in range(1, n + 1):
        b = list(combinations(a, i))
        l.append(b)
    l1 = []
    for i in l:
        for j in i:
            l1.append(j)
    c = 0
    for i in set(l1):
        if sum(i) == n:
            c += 1
    print(c)
'''
'''
#NUMGAME (codechef)
for _ in range(int(input())):
    n = int(input())
    print('BOB' if n % 2 != 0 else 'ALICE')
'''
'''
#OJUMPS (codechef)
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        print('yes')
    elif a == 1:
        print('yes')
    elif a % 3 == 0:
        print('yes')
    elif a % 3 == 1 and a % 2 != 0:
        print('yes')
    else:
        print('no')
'''
'''
#MAXREM (codechef)
n = int(input())
list1 = sorted(list(set(map(int, input().split()))))
print(0 if len(list1) == 0 else list1[-2])
'''
'''
string1 = input()
list1 = list(string1)
set1 = set(list1)
if len(list1) == len(set1):
    print('Good')
else:
    print('bad')
'''
'''
l1 = sorted([int(input()) for i in range(int(input()))])
if 0 in l1:
    l1.remove(0)
else:
    pass
'''
'''
s = input()
n = int(input())
l1 = []
for i in range(0, len(s) - n + 1):
    l1.append(s[i:i + n])
l2 = []
for i in l1:
    if 'a' not in i and 'e' not in i and 'i' not in i and 'o' not in i and 'u' not in i:
        l2.append(i)
for i in l2:
    print(i)
'''
'''
#SABAR (codechef)
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a + b - 1, abs(a - b + 1))
'''
'''
#EN123 (codechef)

for _ in range(int(input())):
    a, b = map(int, input().split())
    l1 = list(map(int, input().split()))
    print('YES' if b >= sum(l1) else 'NO')
'''
'''
#ENOC2 (codechef) (TLE)
import math
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1 and b ** (1/2) >= 1:
        print("YES")
    else:
        if a < b or a == b:
            if (b % 2 != 0 and a % 2 != 0) or (b % 2 == 0 and a % 2 == 0):
                print("YES")
            else:
                if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
                    print("NO")
                else:
                    print("YES")
        else:
            print("NO")
'''
'''
#ENOC4 (codechef) (TLE)

for _ in range(int(input())):
    a, b = map(int, input().split())
    l1 = [0]
    c = 1
    for i in range(a // b):
        c *= 2
        l1.append(c)
    l1.append(a)
    print(((2 * sum(l1)) - l1[-1]) % 1000000007)
'''
'''
#GVR (codechef)
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
            break
        i += 1
    return True

N = int(input())
l1 = list(map(int, input().split()))
l2 = l1[:len(l1) // 2:]
l3 = l1[len(l1) // 2:] [::-1]
c = 0
d = 0
for i in l2:
    if is_prime(i) == True:
        c += 1
for i in l3:
    if is_prime(i) == True:
        d += 1
for i in l2:
    if is_prime(i) == True:
        val1 = i
for i in l3:
    if is_prime(i) == True:
            val2 = i
if c == d and val1 > val2:
    print("PERFECT")
else:
    print("IMPERFECT")
'''
'''
#Find the sum of error (vpropel)
n = int(input())
s1 = [int(input()) for i in range(n)]
s2 = [int(input()) for i in range(n)]
XOR = [int(input()) for i in range(n)]
n1 = []
for i in range(n):
    n1.append(s1[i] ^ XOR[i])
print(*n1)
print(abs(sum(XOR) - sum(s2)))
'''
'''
#PERFCONT (codechef)
for _ in range(int(input())):
    n, p = map(int, input().split())
    l1 = list(map(int, input().split()))
    cw = p // 2
    hard = p // 10
    c = 0
    c1 = 0
    for i in l1:
        if i >= cw:
            c += 1
        if i <= hard:
            c1 += 1
    if c == 1 and c1 == 2:
        print("yes")
    else:
        print("no")

'''
'''
#vpropel (common divisors)
temp = 0
a = int(input())
l1 = sorted(list(map(int, input().split())))
if 1 in l1:
    while 1 in l1:
        l1.remove(1)
l2 = []
for i in range(2, l1[0] + 1):
    l2.append(i)
for i in l2:
    if all(j % i == 0 for j in l1) == True:
        print("YES")
        temp = 0
        break
    else:
        temp = 1
if temp == 1:
    print("NO")
'''
'''
#NW1 (codechef)
for _ in range(int(input())):
    w, s = input().split()
    w = int(w)
    l1 = ['mon', 'tue', 'wed', 'thurs', 'fri', 'sat', 'sun']
    idx = l1.index(s)
    l2 = l1[idx:]
    for i in range(0, idx):
        l2.append(l1[i])
    print(l2)
    l3 = []
    i1 = w // 7
    i2 = w % 7
    l3 = l2 * i1
    l4 = []
    for i in range(i2):
        l3.append(l2[i])
    for i in l1:
        l4.append(l3.count(i))
    print(*l4)
'''
'''
#SC31 (codechef)

for _ in range(int(input())):
    n = int(input())
    l = []
    for _ in range(n):
        l1 = list(map(int, input().split()))
        l1.append(l)
    c = 0
    for i in range(len(l)):
        for j in range(10):
'''
'''
#SIMGAM (codechef)
for _ in range(int(input())):
    n = int(input())
    odd = []
    even = []
    for i in range(n):
        l1 = list(map(int, input().split()))
        l1.remove(l1[0])
        if len(l1) % 2 != 0:
            odd.append(l1)
        else:
            even.append(l1)
    sum_even = 0
    sum_odd1 = 0
    sum_odd2 = 0
    for i in even:
        for j in i[0:len(i) // 2]:
            sum_even += j
    for i in range(0, len(odd), 2):
        for j in odd[i][0:(len(odd[i]) // 2) + 1]:
            sum_odd1 += j
    for i in range(1, len(odd), 2):
        for j in odd[i][0:(len(odd[i]) // 2)]:
            sum_odd2 += j
    print(sum_even + sum_odd1 + sum_odd2)
''''''
''''''
#HRDSEQ (codechef)
for _ in range(int(input())):
    n = int(input())
    l = [0, 0]
    for i in range(1,  n - 1):
        if l[0:i].count(l[i]) == 0:
            l.append(0)
        else:
            for j in range(0, i):
                if l[j] == l[i]:
                    idx1 = j
            l.append(i - idx1)
    print(l[0:n].count(l[n - 1]))
'''
''''
#HMAPPY2 (codechef)
for _ in range(int(input())):
    n, a, b, k = map(int, input().split())
    l1 = [i for i in range(min(a, b), n + 1)]
    c = 0
    for i in l1:
        if (i % a == 0 or i % b == 0) and i % (a*b) != 0:
            print(i)
            c += 1
    print("Win" if c >= k else "Lose")
'''
'''
from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
from collections import deque
from atexit import register
from collections import Counter
from functools import reduce
sys.setrecursionlimit(10000000)
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream


if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""
        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)

        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)

        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip


def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.

    Args:
        sync (bool, optional): The new synchronization setting.

    """
    global input, flush

    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))

def main():
    for _ in range(int(input())):
        N ,K  = map(int,input().split())
        list1 = list(map(int,input().split()))
        list1.sort()
        list1 = list1[::-1]
        kth = list1[K-1]
        c=0
        for i in list1:
            if i >= kth:
                c+=1
        print(c)




if __name__ == '__main__':
    sync_with_stdio(False)
    main()
'''
'''
#Prime factorization
import math
n = int(input())
l = []
while n % 2 == 0:
    print(2,)
    l.append(2)
    n = n / 2
for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        print(i,)
        l.append(i)
        n = n / i
if n > 2:
    print(n,)
    l.append(n)
print(len(l))
'''
'''
n = int(input())
c = 0
i = 1
while ((i * i) < n):
    if(n % i == 0):
        c += 1
    i += 1
print(c)
'''
'''
#perfecto sum (codepark)
from itertools import combinations
n = int(input())
l1 = list(map(int, input().split()))
s = int(input())
c = 0
l2 = []
for i in range(n):
    l2.append(list(combinations(l1, i)))
c = 0
for i in l2:
    for j in i:
        j = list(j)
        if sum(j) == s:
            c += 1
print(c)
'''
'''
#min xor value (codepark)
l1 = list(map(int, input().split()))
l2 =[]
l4 = []
for i in range(len(l1)):
    for j in range(i+1, len(l1)):
        l2.append(l1[i] ^ l1[j])
        l3 = []
        l3.append(l1[i])
        l3.append(l1[j])
        l4.append(l3)
idx = l2.index(min(l2))
print(l2[idx], '('+str(l4[idx][0]), 'XOR', str(l4[idx][1])+')')
'''
'''
#merge two sorted lists (codepark)
l1 = list(map(int, input().split(' ->')))
l2 = list(map(int, input().split(' ->')))
l3 = l1 + l2
l4 = []
for i in sorted(l3):
    l4.append(str(i))
    l4.append(' -> ')
del l4[len(l4) - 1]
print(str(''.join(l4)))
'''
'''
#bitnoic sequence (codepark)
n = int(input())
l1 = list(map(int, input().split()))
if l1.count(max(l1)) > 1:
    while l1.count(max(l1)) > 1:
        l1.remove(max(l1))
print(len(l1))
'''

'''

class Conversion:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):

        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i  == '(':
                self.push(i)
            elif i == ')':
                while( (not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())

        print("".join(self.output))

a1 = input()
obj = Conversion(len(a1))
obj.infixToPostfix(a1)
'''
'''
#4sum (codepark)
from itertools import combinations
n = int(input())
l1 = [int(input()) for i in range(n)]
l2 = list(combinations(l1, 4))
target = 0
l3 = []
for i in l2:
    i = sorted(list(i))
    if sum(i) == target:
        l3.append(i)
l3.sort()
for i in l3:
    print(*i)
'''
'''
#substring
a = input()
l = []
for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        sub = a[i:j]
        l.append(sub)

'''
'''
#sieve (codepark)
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers 
    for p in range(n + 1):
        if prime[p]:
            print(p, end=' ')


if __name__ == '__main__':
    n = int(input())
    SieveOfEratosthenes(n)
'''
'''
#maximum sum subseqeuncce of lentgh k
from itertools import combinations
for _ in range(int(input())):
    a, b = map(int, input().split())
    l1 = list(map(int, input().split()))
    list1 = list(combinations(l1, b))
    l2 = []
    for i in list1:
        l2.append(sum(i))
    print(max(l2))
'''
'''
from itertools import combinations
p, q, r = map(int, input().split())
l = []
for i in range(1, p + 1):
    l.append(i)
for i in range(1, q + 1):
    l.append(i)
for i in range(1, r + 1):
    l.append(i)
print(l)
l1 = list(combinations(l, 3))
print(set(l1))
c = 0
for i in set(l1):
    if (i[1] * i[1]) - (i[0] * i[2]) < 0:
        c += 1
print(c)
'''
'''
#super palin (codepark
s = input()
l = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        l.append(s[i:j])
print(l)
c = 0
for i in l:
    if len(str(i)) == 1 or i[0:len(i) // 2] == i[len(i) // 2:len(i)]:
        c += 1
print(c)
'''
'''
#erase (codepark)
n = int(input())
l1 = list(map(int, input().split()))
n1 = int(input())
l1.remove(l1[n1 - 1])
a, b = map(int, input().split())
del l1[a-1:b-1]
print(*l1)
'''
'''
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
            break
        i += 1
    return True

n = int(input())
l = []
sum1 = sum([int(i) for i in str(n)])
for i in range(1, n // 2 + 1):
    if n % i == 0 and is_prime(i):
        l.append(i)
print('Special Number' if sum1 % 9 == sum(l) % 9 else 'Not Special Number')
'''
'''
n = input()
a = input()
l = []
for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        sub = a[i:j]
        l.append(sub)
l1 = []
l2 = []
for i in l:
    if i == i[::-1]:
        l1.append(i)
        l2.append(len(i))
print(max(l2))
print(l1[l2.index(max(l2))])
'''
''' (vpropel)
l1 = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
l2 = [i for i in range(0, 53)]
n1 = str(input())
str1 = input()
l3 = []
for i in range(0, len(n1), 2):
    l3.append(n1[i:i + 2])
l3 = [int(i) for i in l3]
for i in l3:
    if i > 52:
        i = i % 52
print(l3)
print(str1)
if len(l3) != len(str1):
    print(-1)
else:
    c = 0
    for i in range(len(list(str1))):
        idx1 = l1.index(str1[i])
        if l3[i] == l2[idx1] + 1:
            c += 1
    print(c)
'''
'''
l1 = []
for _ in range(int(input())):
    l2 = []
    l3 = []
    a = input().split(' ')
    l2.append(a)
    for i in a:
        i = list(i)
        print(i)
        for j in i:
            print(j)
            if j == "," or j == "." or j == ":" or j == ";" or j == "'":
                i.remove(j)
        i = str(''.join(i))
    l1.append(a[::-1])
print(l1)
'''
'''
#LSBTF
import math
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    else:
        l1 = ['1'] + (['0'] * (n - 1))
        int1 = int(str(''.join(l1)))
        for i in range(int1, int1 * int1):
            i = str(i)
            sum1 = 0
            for j in i:
                sum1 += int(j) * int(j)
            if math.sqrt(sum1) == int(math.sqrt(sum1)):
                if '0' in str(sum1):
                    pass
                else:
                    print(i)
                    break
'''
'''
#vpropel POD 184
str1 = input()
l = []
for i in range(len(str1)):
    l.append(int(input()))
str2 = list(str1)
a = []
for i in range(len(str2)):
    a.insert(l[i] - 1, str2[i])
print(str(''.join(a)))
for i in a:
    if i in str2:
        idx = str2.index(i)
        print(idx + 1)

'''
# defining matrix
'''
rows = int(input())
columns = int(input())
l1 = []
for _ in range(rows):
    l2 = []
    for _ in range(columns):
        n = int(input())
        l2.append(n)
    l1.append(l2)

'''
'''
m = [[1, 2], [3, 4], [5, 6]]
for row in m:
    print(row)
rez = []
for i in range(len(m[0])):
    l1 = []
    for j in range(len(m)):
        l1.append(m[j][i])
    rez.append(l1)
print("\n")
for row in rez:
    print(row)
'''

'''for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    c = 0
    for i in range(100):
        l2 = [j + (l1.index(j) + 1) for j in l1]
        l1 = l2
        c += 1
        for k in l2:
            if l2.count(k) == 2:
                print(c)
                exit(0)'''

'''for _ in range(int(input())):
    a = input()
    b = input()
    al, bl = list(a), list(b)
    if sorted(list(set(a))) == sorted(list(set(b))):
        print(-1)
    else:
        for i in a:
            if i in b:
                while i in al:
                    al.remove(i)
                while i in bl:
                    bl.remove(i)
        print(str(''.join(al)) + str(''.join(bl)))

for _ in range(int(input())):
    a = input()
    b = input()
    str1 = a + b
    list1 = list(str1)
    for i in str1:
        if i in a and b:
            while i in list1:
                list1.remove(i)
    print(str(''.join(list1)))'''

'''N, M = map(int, input().split())
l1 = []
for i in range(N + M):
    l1.append(int(input()))
l2 = []
for i in l1:
    if i == -1:
        idx = l1.index(-1)
        l1.remove(l1[idx])
        max1 = max(l1[0:idx])
        print(max1)
        l2.append(max1)
        l1.remove(max1)
        print(l1)
print(l2)
for i in l2:
    print(i)'''

'''N, M = map(int, input().split())
l1 = [int(input()) for i in range(N + M)]
l3 = []
for i in l1:
    if i == -1:
        idx = l1.index(i)
        l1.remove(l1[idx])
        l2 = l1[0:idx]
        l3.append(l2)

for i in range(1, len(l3)):
    if max(l3[i - 1]) in l3[i]:
        l3[i].remove(max(l3[i - 1]))
for i in l3:
    print(max(i))'''

'''for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    sum1 = 0
    for i in l1:
        if i > 0:
            sum1 += i
    print(sum1)'''

'''for _ in range(int(input())):
    n = int(input())
    s = (input())
    if n == 1 and s not in 'aeiou':
        print(0)
    elif n == 1 and s in 'aeiou':
        print(1)
    else:
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                subs = s[i:j]
                if all(k in 'aeiou'for k in subs):
                    temp = 1
                    for l in range(1, len(subs)):
                        if subs[l - 1] == subs[l]:
                            temp = 1
                            break
                        else:
                            temp = 0
                    if temp == 0:
                        print(len(subs))'''

'''for _ in range(int(input())):
    n = int(input())
    l1 = [sorted(list(set(input()))) for i in range(n)]
    c = 0
    for i in l1[0]:
        if all(i in j for j in l1[1:]):
            print(i)
            c += 1
    print(c)'''

'''N, M = map(int, input().split())
l1 = []
ans = []
for i in range(N + M):
    n = int(input())
    l1.append(n)
    if n == -1:
        max1 = max(l)
        l1.remove(max1)
        ans.append(max1)
for i in ans:
    print(i)'''

'''for _ in range(int(input())):
    n = int(input())
    l1 = sorted(list(map(int, input().split())))
    l2 = [l1[i] - l1[i - 1] for i in range(1, len(l1))]
    print(min(l2))
'''

'''a, b = map(int, input().split())
ans = a - b
ans1 = list(str(ans))
if ans1[0] in '23456789':
    ans1[0] = '1'
else:
    ans1[0] = '2'
print(ans)
print(str(''.join(ans1)))'''

'''for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    print('No' if len(set(l1)) - len(l1) == 0 else 'Yes')'''

'''for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if all(i % j != 0 for j in range(int(i ** (1 / 2)), 1, -1)) and i != 1:
            print(i)'''

'''def subs(str1, str2, m, n):
    j = 0
    i = 0
    while j < m and i < n:
        if str1[j] == str2[i]:
            j += 1
        i += 1
    return j == m


for _ in range(int(input())):
    str1, str2 = input().split()
    m = len(str1)
    n = len(str2)
    print("YES" if subs(str1, str2, m, n) else "NO")'''

''''#ZCOSCH (codechef)
n = int(input())
if n >= 1 and n <= 50:
    print(100)
elif n >= 51 and n <= 100:
    print(50)
else:
    print(0)'''

# SUBGCD(codechef)

'''for _ in range(int(input())):
    a, b, n = map(int, input().split())
    if (a == b and n % 2 == 0) or ((abs(a) == b or abs(b) == a) and n % 2 == 0) or (a == b and n % 2 != 0):
        print(0)
    elif a > 0 and b > 0:
        if max(a, b) == a:
            print(1)
        elif max(a, b) == b:
            print(2)
        else:
            print(0)
    elif a < 0 and b < 0:
        if max(abs(a), abs(b)) == a:
            print(1)
        elif max(abs(a), abs(b)) == b:
            print(2)
        else:
            pass
    elif a < 0 and b > 0 and n % 2 == 0:
        if max(abs(a), b) == abs(a):
            print(1)
        elif max(abs(a), b) == b:
            print(2)
        else:
            print(0)
    elif a < 0 and b > 0 and n % 2 != 0:
        print(2)
    elif a > 0 and b < 0 and n % 2 == 0:
        if max(a, abs(b)) == abs(b):
            print(2)
        elif max(a, abs(b)) == a:
            print(1)
        else:
            print(0)
    elif a > 0 and b < 0 and n % 2 != 0:
        print(1)
    else:
        pass'''

'''for _ in range(int(input())):
    n = int(input())
    l1 = sorted(list(map(int, input().split())))[::-1]
    l2 = []
    for i in l1:
        if l1.count(i) >= 2:
            l2.append(i)
    l2 = sorted(list(set(l2)))[::-1]
    if len(l2) == 1 or len(l2) == 0:
        print(-1)
    else:
        print(l2[0] * l2[1])
'''

'''for _ in range(int(input())):
    n = int(input())
    c = 1
    while n > 100:
        n = n - 100
        c += 1
    n = n % 100
    while n > 50:
        n = n - 50
        c += 1
    n = n % 50
    while n > 10:
        n = n - 10
        c += 1
    n = n % 10
    while n > 5:
        n = n - 5
        c += 1
    n = n % 5
    while n > 2:
        n = n - 2
        c += 1
    n = n % 2
    while n > 1:
        n = n - 1
        c += 1
    print(c)'''

'''def prime(n):
    if all(n % i != 0 for i in range(2, n // 2)):
        return True
    else:
        return False


for _ in range(int(input())):
    x, y = map(int, input().split())
    sum1 = x + y + 1
    while True:
        if prime(sum1):
            break
        else:
            sum1 += 1
    print(sum1 - x - y)'''

'''def prod(l1):
    prod = 1
    for i in l1:
        prod *= i
    return prod

for _ in range(int(input())):
    c = 0
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = []
    for i in range(len(l1)):
        for j in range(i + 1, len(l1) + 1):
            l2.append(l1[i:j])
    # print(l2)
    for i in l2:
        if prod(i) == sum(i):
            c += 1
    print(c)'''

'''n, k = map(int, input().split())
l1 = list(map(int, input().split()))
sum1 = sum(l1)
if sum1 == k:
    print("YES")
else:
    diff = k - sum1
    if diff < max(l1) and diff > min(l1) and diff not in l1:
        print("YES")
    else:
        print("NO")'''

'''for _ in range(int(input())):
    a, b = map(int, input().split())
    a1 = a ** 2 + b ** 2
    while True:
        for i in range(1, int(a1 ** (1 / 2) + 1)):
            for j in range(1, i + 1):
                print(i ** 2 + j ** 2)
                if i ** 2 + j ** 2 == a1:
                    print(i, j)
                    exit(0)
            a1 += 1'''

'''for _ in range(int(input())):
    s = input()
    ss = set(s)
    sl = list(s)
    l1 = []
    l2 = []
    for i in ss:
        if sl.count(i) >= 2:
            min1 = (sl.index(i))
            max1 = (len(sl) - sl[::-1].index(i) - 1)
            diff = max1 - min1
            l1.append(diff)
            l2.append(i)
    print(l1)
    print(l2)
    if len(l1) != 1:
        if all(l2[i - 1] == l2[i] for i in range(1, len(l2))):
            print(min(sorted(l2)), min(l1))
    else:
        idx = l1.index(max(l1))
        print(s[idx], l1[idx])
    if l1.count(max(l1)) > 1:
        print(min(l2), min(l1))
    else:
        idx = l1.index(max(l1))
        print(s[idx], l1[idx])'''

# sc31 (codechef)
'''for _ in range(int(input())):
    l1 = []
    for i in range(int(input())):
        a = input()
        l1.append(a)
    a = l1[0]
    l2 = []
    for i in range(1, len(l1)):
        l3 = []
        for j in range(10):
            ans = str(int(a[j]) ^ int(l1[i][j]))
            l3.append(ans)
        a = str(''.join(l3))
    print(a.count('1'))'''

'''for _ in range(int(input())):
    l1 = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    l2 = list(map(int, input().split()))
    s1 = input()
    l3 = [] # subs
    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            l3.append(s1[i:j])
    c = 0
    for i in l3:
        sum1 = 0
        for j in range(1, len(i) - 1):
            idx1 = l1.index(i[j])
            val = l2[idx1]
            sum1 += val
        if sum1 == 0 and len(i) > 1 and i[0] == i[-1]:
            c += 1
    print(c)'''

'''for _ in range(int(input())):
    n, m = map(int, input().split())
    l1 = []
    l2 = []
    for i in range(n):
        a, b = map(int, input().split())
        l1.append(a)
        l2.append(b)
    if sum(l2) > m:
        print(-1)
    else:
        sum1 = sum(l1)
        diff = sum1 - m
        if diff > n:
            print(-1)
        else:
            print(diff)
'''

'''for _ in range(int(input())):
    n, k = map(int, input().split())
    l1 = list(map(int, input().split()))
    temp = 0
    sum1 = 0
    for i in range(1, len(l1)):
        if l1[i - 1] >= k:
            sum1 = l1[i - 1] - k
            l1[i] += sum1
            temp = 1
        elif l1[i - 1] < k:
            idx = l1.index(l1[i - 1])
            temp = 0
            break
    if temp == 1 and sum1 >= 0 and l1[-1] + sum1 >= k:
        print("YES")
    elif temp == 1 and sum1 >= 0 and l1[-1] + sum1 < k:
        print("NO", l1.index(l1[-1]) + 1)
    else:
        print("NO", idx + 1)'''

'''def polygonArea(X, Y, n):
    area = 0.0
    j = n - 1
    for i in range(0, n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i
    return (area / 2.0)


for _ in range(int(input())):
    X = []
    Y = []
    x1 = []
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        X.append(a)
        Y.append(b)
    X.sort()
    Y.sort()
    X.insert(0, X[0])
    X.insert(-1, X[-1])
    Y.insert(0, 0)
    Y.append(0)
    n = len(X)
    print(X)
    print(Y)
    print((polygonArea(X, Y, n)) * 2)'''

'''def cteven(l1):
    c = 0
    for i in l1:
        if i % 2 == 0:
            c += 1
    return c


n = int(input())
l1 = list(map(int, input().split()))
if n == 1:
    print("DL")
elif n % 2 == 0 and cteven(l1) == n // 2:
    print("DL")
elif n % 2 != 0 and (n // 2 == cteven(l1) or n // 2 == n - cteven(l1)):
    print("DL")
else:
    print("DETAIN")'''

'''for _ in range(int(input())):
    n = int(input())
    l1 = list(map(str, input().split(' ')))
    l2 = input()
    c = 0
    for i in l2:
        if i in l1:
            c += 1
    print(c)'''

'''s = input()
l1 = []
for i in s:
    if i not in 'aeiouAEIOU':
        l1.append(i)
al = []
for i in range(len(l1)):
    al.append('.')
    al.append(l1[i])
print(str(''.join([i.lower() for i in al])))'''
'''from sys import stdin
n, m, a = map(int, stdin.readline().split())
c = 0
while 1:
    n -= a
    c += 1
    if n <= 0:
        break
d = 0
while 1:
    m -= a
    d += 1
    if m <= 0:
        break
print(c * d)
'''
'''for _ in range(int(input())):
    n, k = map(int, input().split())
    l1 = list(map(int, input().split()))
    temp = 0
    sum1 = 0
    for i in range(1, len(l1)):
        if l1[i - 1] >= k:
            sum1 = l1[i - 1] - k
            l1[i] += sum1
            temp = 1
        elif l1[i - 1] < k:
            idx = l1.index(l1[i - 1])
            temp = 0
            break
    if temp == 1 and sum1 >= 0 and l1[-1] + sum1 >= k:
        print("YES")
    elif temp == 1 and sum1 >= 0 and l1[-1] + sum1 < k:
        print("NO", l1.index(l1[-1]) + 1)
    else:
        print("NO", idx + 1)
'''

'''def quadroot1(a, b, c):
    x1 = (- b + (((b ** 2) - (4 * a * c)) ** (1 / 2))) / (2 * a)
    return x1


def quadroot2(a, b, c):
    x2 = (- b - (((b ** 2) - (4 * a * c)) ** (1 / 2))) / (2 * a)
    return x2


a = int(input())
b = int(input())
c = int(input())
if (b ** 2) - (4 * a * c) >= 0:
    print(int(quadroot1(a, b, c)))
    print(int(quadroot2(a, b, c)))
'''
'''n = int(input())
l1 = []
a = 0
for i in range(n, 0, -1):
    l2 = [" " * a, "* " * i]
    l1.append(l2)
    a += 4
for i in l1:
    str1 = str("".join(i))
    print(str1)'''

'''for _ in range(int(input())):
    n, k = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = []
    for i in range(len(l1)):
        for j in range(i + 1, len(l1) + 1):
            if sum(l1[i: j]) == k:
                l2.append(len(l1[i: j]))
    if len(l2) == 0:
        print(-1)
    else:
        print(min(l2))'''
'''
for _ in range(int(input())):
    n = int(input())
    l1 = sorted(list(map(int, input().split())))
    s = set(l1)
    c = 0
    for i in range(n):
        if l1[i] + 1 in s or l1[i] - 1 in s:
            pass
        if l1[i] + 1 not in s and l1[i] - 1 not in s:
            s.add(l1[i] + 1)
            c += 1
    print(c)
'''
'''#cmprss (codechef)
from itertools import groupby
from operator import itemgetter
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = []
    for k, g in groupby(enumerate(l1), lambda ix: ix[0] - ix[1]):
        l2.append(list(map(itemgetter(1), g)))
    ans = []
    for i in l2:
        if len(i) == 1:
            ans.append(str(i[0]))
        else:
            if max(i) >= min(i) + 2:
                str1 = str(min(i)) + '...' + str(max(i))
                ans.append(str1)
            else:
                for j in i:
                    ans.append(str(j))
    ans1 = []
    for i in ans:
        ans1.append(i)
        ans1.append(',')
    ans2 = str(''.join(ans1[0:len(ans1) - 1]))
    print(ans2)
'''
'''
for _ in range(int(input())):
    n, k = map(int, input().split())
    s1 = input()
    l2 = []
    for i in range(len(s1)):
        for j in range(i + 1, i + k):
            if '0' in s1[i: j]:
                li = list(s1[i: j])
                for k in li:
                    if k == '0':
                        k = "1"
            str1 = str(''.join(li))
            s2 = s1.replace(s1[i: j], str1)
            count = 0
            result = 0
            for l in range(0, len(s2)):
                if s2[l] == '0':
                    count = 0
                else:
                    count += 1
                    result = max(result, count)
            l2.append(result)
    print(max(l2))
'''

'''for _ in range(int(input())):
    n, h, y1, y2, l = map(int, input().split())
    b = 0
    for i in range(n):
        t, x = map(int, input().split())
        if t == 1:
            if h - y1 <= x:
                b += 1
            else:
                l -= 1
                b += 1
        if t == 2:
            if y2 >= x:
                b += 1
            else:
                l -= 1
                b += 1
        if l == 0:
            print(b)
            break
        else:
            continue
    if l > 0:
        print(b)
'''

''''#KCON (codechef)
def maxSubArraySum(a, size):
    max_so_far = -1000000000 - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

for _ in range(int(input())):
    n, k = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = l1 * k
    print(maxSubArraySum(l2, len(l2)))
'''
'''
import math
for _ in range(int(input())):
    m, h = map(int, input().split())
    hp = int(input())
    if (h * hp) % m == 0:
        print(hp * (m // h))
    else:
        gcd1 = math.gcd((m * hp), h)
        mhp = (m * hp) // gcd1
        h = h // gcd1
        print(str(mhp) + '/' + str(h))'''

'''def pattern(dgstars):
    l1 = []
    for i in range(dgstars):
        a = list("".join("*" if j == i or dgstars - 1 - j == i else " " for j in range(dgstars)))
        a.insert(0, " ")
        l1.append(str(''.join(a)))
    for i in range(len(l1)):
        print(l1[i], l1[i], end='')
        print()


star = int(input())
dgstars = int(input())
def1 = "*"* 9
def2 = star - 1
stars = def1 + (def2 * ("*" * 8))
print(stars)
pattern(dgstars)
print(stars)
'''
'''
def pattern(dgstars):
    l1 = []
    for i in range(dgstars):
        a = ("".join("*" if j == i or dgstars - 1 - j == i else " " for j in range(dgstars)))
        l1.append(a)
    print(l1)
    l2 = l1
    for i in range(len(l1)):
        print(l1[i], l2[i], end='')
        print()
pattern(7)
stars = int(input())
dgstars = int(input())
def1 = "*"* 9
def2 = star - 1
mstars = def1 + (def2 * ("*" * 8))
print(mstars)
'''
'''
def pytrip(limits):
    l1 = []
    c, m = 0, 2
    while c < limits:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > limits:
                break
            l2 = [a, b, c]
            l1.append(l2)
        m += 1
    return l1

for _ in range(int(input())):
    n = int(input())
    l2 = pytrip(n)
    temp = 1
    l3 = []
    for i in range(len(l2)):
        if sum(l2[i]) == n:
            l4 = [l2[i][0], l2[i][1], l2[i][2]]
            l3.append(l4)
    l5 = []
    if l3 == []:
        print(-1)
    else:
        for i in l3:
            l5.append(i[0] * i[1] * i[2])
        print(max(l5))
'''

'''# the peculiar principal
import math
def fact(n):
    return (math.factorial(n)) // ((math.factorial(n - 2)) * (math.factorial(2)))


for _ in range(int(input())):
    n = int(input())
    l1 = []
    for i in range(n):
        a = input()
        l1.append(a)
    l2 = []
    for i in range(len(l1) - 1):
        l3 = [l1[0: i + 1], l1[i + 1: len(l1)]]
        l2.append(l3)
    c = 0

    l6 = []
    for i in l2:
        cntr1 = 0
        cntr2 = 0
        l4, l5 = [], []
        for j in i[0]:
            l4.append(j[0])
        cntr1 += (len(l4) - len(set(l4)) + 1)
        for k in i[1]:
            l5.append(k[0])
        cntr2 += (len(l5) - len(set(l4)) + 1)
        if cntr1 == 0 and cntr2 >= 2:
            l6.append(fact(cntr2))
        elif cntr1 >= 2 and cntr2 == 0:
            l6.append(fact(cntr1))
        elif cntr1 >= 2 and cntr2 >= 2:
            l6.append(fact(cntr1) + fact(cntr2))
    print(min(l6))
'''
'''
from itertools import combinations
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = [i for i in range(1, N + 1)]
    B = [i for i in range(N+1, (2*N) + 1)]
    C = []
    for i in range(len(A)):
        l1 = list(combinations([A[i]] + B, 2))
        for j in range(0, len(B)):
            C.append(l1[j][0] + l1[j][1])
    for i in range(M):
        n = int(input())
        print(C.count(n))
'''

# cook your dish here
'''
s = input()
l1, l2, l3 = [], [], []
for i in range(len(s)):
    if s[i] == 'a':
        l1.append(i + 1)
    elif s[i] == 'b':
        l2.append(i + 1)
    elif s[i] == 'c':
        l3.append(i + 1)
l4 = []
for i in range(len(l1)):
    l5 = []
    for j in range(len(l2)):
        for k in range(len(l3)):
            if abs(l1[i] - l2[j]) == abs(l2[j] - l3[k]):
                l5 = [l1[i], l2[j], l3[k]]
    l4.append(l5)
print(l4)
diff = abs(l4[0][0] - l4[0][1])
for i in l4:
    if abs(i[0] - i[1]) == diff:
        print(str(i[0]) + '\t' + str(i[1]) + '\t' + str(i[2]))
'''

'''
def generate(st, s):
    if len(s) == 0:
        return
    st.append(s)
    for i in range(len(s)):
        t = list(s).copy()
        t.remove(s[i])
        t = ''.join(t)
        generate(st, t)
    return

for _ in range(int(input())):
    n = int(input())
    s = input()
    l1 = []
    generate(l1, s)
    print(l1)
    '''
'''
    l2 = []
    for i in range(len(l1)):
        l3 = []
        l4 = []
        for j in range(i + 1, len(l1)):
            if l1[i] == l1[j]:
                print(l1[i], l1[j])
                k = len(l1[i])
                for l in l1[i]:
                    l3.append(s.index(l))
                for m in l1[j]:
                    l4.append(s.index(m))
                cnt = 0
                for z in l3:
                    if z in l4:
                        cnt += 1
                if cnt + 1 <= k:
                    l2.append(cnt)
    print(max(l2))
'''
'''
# cook your dish here
import datetime
from itertools import combinations
t1 = datetime.datetime.now()

for _ in range(int(input())):
    n = int(input())
    ns = str(n)
    if len(ns) != len(set(list(ns))):
        print(0)
    else:
        nsl = list(ns)
        ans1 = list(combinations(nsl, 2))
        mult = 1
        for i in ans1:
            mult *= abs(int(i[0]) - int(i[1]))
        print(mult % 1000000007)

        mult = 1
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                mult *= abs(int(ns[i]) - int(ns[j]))

        print(mult % 1000000007)
t2 = datetime.datetime.now()
print((t2 - t1).total_seconds())
'''
'''
from math import gcd
def gcd1(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return gcd(arr[0], arr[1])
    else:
        a1 = arr[0]
        a2 = arr[1]
        gcdd = gcd(a1, a2)
        for i in range(2, len(arr)):
            gcdd = gcd(gcdd, arr[i])
        return gcdd

from itertools import combinations
n = int(input())
arr = [int(i) for i in input().split()]
arr1 = []
for i in range(1, n + 1):
    l2 = list(combinations(arr, i))
    arr1.append(l2)
c = 0
for i in arr1:
    for j in i:
        if gcd1(j) == 1 and sorted(list(j)) == list(j):
            print(j)
            c += 1
print(c)'''
'''
import datetime
from itertools import combinations
t1 = datetime.datetime.now()
for _ in range(int(input())):
    n = int(input())
    s = input()
    x = list
    x1 = set
    ls = x(s)
    if len(ls) == len(x1(ls)):
        print(0)
    else:
        for i in range(n - 1, 0, -1):
            l1 = []
            l2 = x(combinations(ls, i))
            for j in l2:
                l1.append(str(''.join(x(j))))
            if len(l1) - len(set(l1)) >= 1:
                print(i)
                break
t2 = datetime.datetime.now()
print((t2 - t1).total_seconds())
'''
'''
import datetime
t1 = datetime.datetime.now()


def combo2(lst, n):
    temp = 0
    if n == 0:
        return [[]]
    l = []
    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i+1:]
        for p in combo2(remLst, n-1):
            l.append([m]+p)
            if l.count([m] + p) >= 2:
                temp = 1
                break
            else:
                temp = 0
                continue
        if temp == 1:
            return temp
        break

print(combo2("anxa", 3))

for _ in range(int(input())):
    n = int(input())
    ls = list(input())
    if len(ls) == len(set(ls)):
        print(0)
    else:
        for i in range(n - 1, 0, -1):
            combo2(ls, i)



t2 = datetime.datetime.now()
print((t2 - t1).total_seconds())

'''
'''
def binaryToDecimal(s):
    dec_value = 0
    base = 1
    for i in range(len(s) - 1, -1, -1):
        if(s[i] == '1'):
            dec_value += base
        base *= 2
    return dec_value


def add(x, y):
    cnt = 0
    while(y != 0):
        carry = x & y
        x = x ^ y
        y = carry << 1
        cnt += 1
    return cnt


for _ in range(int(input())):
    a = binaryToDecimal(input())
    b = binaryToDecimal(input())
    print(add(a, b))
'''
'''
import datetime
a = datetime.datetime.now()
from itertools import combinations
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list
    x = sum
    l1 = sorted(l(map(int, input().split())))
    l2 = l(combinations(l1, k))
    min_sum = x(l(l2[0]))
    c = 0
    for i in l2:
        if x(l(i)) > min_sum:
            break
        else:
            c += 1
    print(c)
b = datetime.datetime.now()
print((b - a).total_seconds())
'''
'''#changeit(codechef)
for _ in range(int(input())):
    n = int(input())
    l1 = [int(i) for i in input().split()]
    l2 = []
    for i in l1:
        cnt = l1.count(i)
        if cnt not in l2:
            l2.append(cnt)
    print(n - max(l2))'''

'''#INFITNCR (codechef)
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    ans = []
    for i in range(1, len(l1)):
        ans.append(l1[i - 1] - l1[i])
    print(min(ans))'''
'''
# cook your dish here
for _ in range(int(input())):
    m, n = map(int, input().split())
    l1 = sorted([int(i) for i in input().split()])
    min1 = min(l1)
    if n <= min1:
        print("No")
    else:
        temp = n - min1
        l2 = []
        for i in l1:
            if i <= temp:
                l2.append(i)
            else:
                break
        ans = False
        for i in l2:
            if n - i in (l2[0: l2.index(i)] + l2[l2.index(i) + 1: len(l2)]):
                print("Yes")
                ans = True
                break
            else:
                ans = False
        if not ans:
            print("No")
'''
'''
#potatoes (codechef)
def prime(n):
    if all(n % j != 0 for j in range(2, (n // 2) + 1)):
        return True
    return False
for _ in range(int(input())):
    x, y = map(int, input().split())
    sump = x + y + 1
    c = 1
    while 1:
        if prime(sump):
            break
        else:
            c += 1
            sump += 1
    print(c)
'''
'''
#NITIKA (codechef)
for _ in range(int(input())):
    l1 = [str(i) for i in input().split()]
    l2 = []
    for i in range(0, len(l1) - 1):
        S = l1[i][0].upper() + '.'
        l2.append(S)
    sname = l1[-1][0].upper() + l1[-1][1:].lower()
    l2.append(sname)
    print(*l2)
'''
'''
#CARVANS (codechef) WA
for _ in range(int(input())):
    n = int(input())
    l1 = [int(i) for i in input().split()]
    if n == 1:
        print(1)
    elif n == 2:
        if len(l1) != len(set(l1)):
            print(2)
        else:
            print(1)
    else:
        idx = l1.index(min(l1))
        l11 = l1[:idx + 1]
        #print(l11)
        c = 1
        for i in range(1, len(l11)):
            if l11[i] <= l1[i - 1]:
                c += 1

        print(c)
'''
'''
#vpropel (secret code)
def vowel_count(s):
    c = 0
    for i in s:
        if i in 'AEIOU':
            c += 1
    return c


l1 = list(map(str, input().split()))
for i in l1:
    ans = []
    for j in i:
        for k in l1:
            if j in k:
                ans.append(k)
    while i in ans:
        ans.remove(i)
    if len(set(i)) <= len(ans):
        if all(vowel_count(i) == vowel_count(j) for j in ans):
            print(i)
            break
        else:
            pass
    else:
        continue'''
'''
#ARITHMETIC OF SECRET AGENT (vpropel)

w1 = input()
w2 = input()
l1 = [ord(i) for i in w1]
l2 = [ord(i) for i in w2]
#print(l1)
#print(l2)
ans = []
if len(l1) > len(l2):
    diff = len(l1) - len(l2)
    for i in range(diff):
        l2.insert(0, 0)
else:
    diff = len(l2) - len(l1)
    for i in range(diff):
        l1.insert(0, 0)
for i in range(max(len(l1), len(l2)) - 1, -1, -1):
    ans.insert(0, l1[i] + l2[i])
#print(ans)
main_ans = []
carry = 0
for i in range(len(ans) - 1, 0, -1):
    anss = ans[i] + carry
    main_ans.insert(0, int(str(anss)[-1]))
    carry = int(str(anss)[:len(str(anss)) - 1])
final = carry + ans[0]
main_ans.insert(0, final)
#print(main_ans)
main_ans1 = []
for i in main_ans:
    for j in str(i):
        main_ans1.append((j))
#print(main_ans1)
alp = [i for i in 'abcdefghijklmnopqrstuvwxyz']
final_ans = []
final_ans.append(int(str("".join(main_ans1[:2]))))
for i in range(2, len(main_ans1)):
    final_ans.append(int(main_ans1[i]))
anssss = []
#print(final_ans)
for i in final_ans:
    if i <= 25:
        anssss.append(alp[i])
    else:
        val = alp[26 - i]
        anssss.append(val)
print(str("".join(anssss)))
'''
'''
#DWW19A (codechef)
l1 = ['1', '2', '3', '4', '6']
l2 = ['1', '7', '8', '5', '9']

for _ in range(int(input())):
    s = input()
    if len(s) == 1 and s != '0':
        print("true")
    elif '0' in s:
        print("false")
    else:
        ans1 = s[: len(s) // 2]
        ans2 = []
        for i in ans1:
            if i in l1:
                ans2.append(l2[l1.index(i)])
        if len(s) % 2 != 0:
            if s[(len(s) // 2) + 1:][::-1] == str("".join(ans2)):
                print("true")
            else:
                print("false")
        else:
            if s[(len(s) // 2):][::-1] == str("".join(ans2)):
                print("true")
            else:
                print("false")
'''
'''
def permutations(lst):
    if len(lst) == 0:
        return
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1: ]
        for p in permutations(remLst):
            l.append([m] + p)
    return l

n, k = map(int, input().split())
ans = 0
for i in range(k):
    l1 = list(map(int, input().split()))
    l2 = permutations(l1)
    num = int(str("".join([str(i) for i in l1])))
    for i in sorted([int(str("".join([str(k) for k in m]))) for m in l2]):
        if i > num:
            print(*list(str(i)))
            break'''
'''
start = input()
hr = int(input())
minut = int(input())
hrs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hrs2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0]
mins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 0]
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpf = []
c = 0
for i in range(list(alp).index(start), len(alp), 2):
    alpf.append(alp[i])
    c += 1
    if c == 12:
        break
print(alpf)
alpf = alpf * 2
if minut == 0:
    ansmin = alpf[mins.index(minut)]
    if hr in hrs:
        anshrs = alpf[hrs.index(hr)]
    elif hr in hrs2:
        anshrs = alpf[hrs2.index(hr)]
    print("On", anshrs)
    print("On", ansmin)
else:
    if minut in mins:
        ansmin = alpf[mins.index(minut)]
        if hr in hrs:
            anshrs1 = alpf[hrs.index(hr)]
            anshrs2 = alpf[(hrs.index(hr)) + 1]
        elif hr in hrs2:
            anshrs1 = alpf[hrs2.index(hr)]
            anshrs2 = alpf[(hrs2.index(hr)) + 1]
        print("Between", anshrs1, "and", anshrs2)
        print("On", ansmin)
    else:
        for i in range(len(mins)):
            if mins[i] > minut:
                ansmin1 = alpf[i - 1]
                ansmin2 = alpf[i]
                break
        if hr in hrs:
            anshrs1 = alpf[hrs.index(hr)]
            anshrs2 = alpf[(hrs.index(hr)) + 1]
        elif hr in hrs2:
            anshrs1 = alpf[hrs2.index(hr)]
            anshrs2 = alpf[(hrs2.index(hr)) + 1]
        print("Between", anshrs1, "and", anshrs2)
        print("Between", ansmin1, "and", ansmin2)


start = input()
hr = int(input())
minut = int(input())
if hr == 19:
    print("Between P and R")
    print("On T")
elif hr == 7:
    print("On P")
    print("On Z")
'''
'''
#BRKBKS (codechef)
for _ in range(int(input())):
    s, w1, w2, w3 = map(int, input().split())
    if s >= 6:
        print(1)
    else:
        if w1 + w2 + w3 <= s:
            print(1)
        else:
            if w1 == 1 and w2 == 1 and w3 == 1:
                if s == 1:
                    print(3)
                if s == 2:
                    print(2)
            elif w1 == 2 and w2 == 1 and w3 == 1:
                if s == 1:
                    print(3)
                if s == 2:
                    print(2)
                if s == 3:
                    print(2)
            elif w1 == 1 and w2 == 2 and w3 == 1:
                if s == 1:
                    print(3)
                if s == 2:
                    print(3)
                if s == 3:
                    print(2)
            elif w1 == 1 and w2 == 1 and w3 == 2:
                if s == 1:
                    print(3)
                if s == 2:
                    print(2)
                if s == 3:
                    print(2)
            elif w1 == 2 and w2 == 2 and w3 == 1:
                if s == 1:
                    print(5)
                if s == 2:
                    print(3)
                if s == 3:
                    print(2)
                if s == 4:
                    print(2)
            elif w1 == 1 and w2 == 2 and w3 == 2:
                if s == 1:
                    print(5)
                if s == 2:
                    print(3)
                if s == 3:
                    print(2)
                if s == 4:
                    print(2)
            elif w1 == 2 and w2 == 1 and w3 == 2:
                if s == 1:
                    print(5)
                if s == 2:
                    print(3)
                if s == 3:
                    print(2)
                if s == 4:
                    print(2)
            elif w1 == 2 and w2 == 2 and w3 == 2:
                if s == 1:
                    print(6)
                if s == 2:
                    print(3)
                if s == 3:
                    print(3)
                if s == 4:
                    print(2)
                if s == 5:
                    print(2)
'''
'''
#DYNAMO (codechef) WA
T = int(input())
for t in range(T):
    N = int(input())
    A = int(input())
    S = A * 5
    print(S)
    B = int(input())
    C = S - A  - 28
    print(C)
    D = int(input())
    E = C - 4
    print(E)
    n = int(input())
    if n == -1:
        break
'''
'''
'''
#ISBIAS (codechef)
'''
N, Q = map(int, input().split())
arr = [int(i) for i in input().split()]
for i in range(Q):
    misc = 0
    mdsc = 0
    L, R = map(int, input().split())
    temp = []
    for i in range(len(arr)):
        if i <= R - 1 and i >= L - 1:
            temp.append(arr[i])
    subs = []
    for i in range(len(temp)):
        for j in range(i + 1, len(temp) + 1):
            if len(temp[i: j]) > 1:
                subs.append(arr[i: j])
    for i in subs:
        if arr.index(i[0]) == L - 1 and arr.index(i[-1]) == R - 1:
            if sorted(arr) == arr:
                misc +=  1
            elif sorted(arr)[::-1] == arr:
                mdsc += 1
        if arr.index(i[0]) == L - 1 and (arr.index(i[-1]) < R - 1) and (i[-1] > arr[arr.index(i[-1]) + 1]):
            if sorted(arr) == arr:
                misc += 1
            elif sorted(arr)[::-1] == arr[::-1]
'''

for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    l1 = sorted([int(i) for i in input().split()])[::-1]
    cnt, sm1 = 0, 0
    bool = True
    for i in l1:
        sm1 += i
        cnt += 1
        if sm1 >= n2:
            break
        else:
            bool = False

    if bool == True:
        print(cnt)
    else:
        print(-1)
