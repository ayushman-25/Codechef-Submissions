from collections import defaultdict
mod = 1 << 32
n, q = map(int, input().split())
weights1 = [int(i) for i in input().split()]
weights2 = [(i % mod * i % mod) % mod for i in weights1]
myDP1 = [1] * (n)
myDP2 = [1] * (n)
myDD = defaultdict(int)
for i in range(n - 1):
    u, v = map(int, input().split())
    myDD[v - 1] = u - 1
    if(u == 1):
        myDP1[u - 1] = (weights1[u - 1] % mod)
        myDP2[u - 1] = (weights2[u - 1] % mod)
        # val = (weights1[v - 1] % mod * weights1[myDD[v - 1]] % mod) % mod
        myDP1[v - 1] = (weights1[v - 1] % mod * weights1[myDD[v - 1]] % mod) % mod
        myDP2[v - 1] = (weights2[v - 1] % mod * weights2[myDD[v - 1]] % mod) % mod
    else:
        if(myDP1[u - 1] == 1):
            # val = (weights1[u - 1] % mod * weights1[myDD[u - 1]] % mod) % mod
            myDP1[u - 1] = (weights1[u - 1] % mod * weights1[myDD[u - 1]] % mod) % mod
        if(myDP2[u - 1] == 1):
            myDP2[u - 1] = (weights2[u - 1] % mod * weights2[myDD[u - 1]] % mod) % mod
        # val = (weights1[v - 1] % mod * myDP1[u - 1] % mod) % mod
        myDP1[v - 1] = (weights1[v - 1] % mod * myDP1[u - 1] % mod) % mod
        myDP2[v - 1] = (weights2[v - 1] % mod * myDP2[u - 1] % mod) % mod

print(myDP1)
print(myDP2)
for _ in range(q):
    u, v = map(int, input().split())

    if(myDD[u - 1] == myDD[v - 1]):
        t1 = ((weights1[u - 1] % mod * weights1[v - 1] % mod) % mod)
        t2 = (t1 % mod + myDP2[myDD[u - 1]] % mod) % mod
        print(t2)