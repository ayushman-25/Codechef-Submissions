from random import *
import sys
# orig_stdin = sys.stdin
# orig_stdout = sys.stdout
# f1 = open("D:\\n1\\New folder\\cp\\in.txt", 'r')
# f2 = open("D:\\n1\\New folder\\cp\\in.txt", 'w')
# sys.stdin = f1
# sys.stdout = f2
t = randint(1, int(1e1))
print(t)
for _ in range(t):
    n = randint(1, int(1e1))
    arr = [randint(1, int(1e9)) for _ in range(n)]
    print(n)
    print(*arr)
# sys.stdin = orig_stdin
# sys.stdout = orig_stdout
# f1.close()
# f2.close()