from sys import stdin,stdout

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

for _ in range(int(stdin.readline())):
    n, q = map(int,stdin.readline().split())
    arr = [int(k) for k in stdin.readline().split()]
    prefix=[0] * (n+1)
    suffix=[0] * (n+2)
    for i in range(1, n + 1):
        prefix[i] = gcd(arr[i - 1],prefix[i - 1])
    for i in range(n, 0, -1):
        suffix[i] = gcd(arr[i - 1], suffix[i + 1])
    for i in range(q):
        l, r = map(int,stdin.readline().split())
        res = gcd(prefix[l - 1],suffix[r + 1])
        stdout.write(str(res) + "\n")


