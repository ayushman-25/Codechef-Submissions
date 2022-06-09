from collections import defaultdict
dd = defaultdict(str)
for i in range(int(input())):
    a, b = input().split()
    dd[a] = b
q = int(input())
s = input()
for i in dd.keys():
    if i == s and q == 1:
        print(dd[i]); exit(0)
    if dd[i] == s and q == 2:
        print(i); exit(0)