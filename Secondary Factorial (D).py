from math import factorial as f, prod
k, s = int(input()), 1
while 1:
    if f(s) > k:
        print(-1); exit(0)
    if f(s) == k:
        print(prod([i for i in range(2 - (s & 1), s + 1, 2)])); exit(0)
    s += 1
