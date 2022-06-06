'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
# from collections import *
# from itertools import *
# from math import *
# from queue import *
# from heapq import *
# from bisect import *
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
readint = lambda: int(sys.stdin.readline().rstrip("\r\n"))
readints = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split())
readstr = lambda: sys.stdin.readline().rstrip("\r\n")
readstrs = lambda: map(str, sys.stdin.readline().rstrip("\r\n").split())
readarri = lambda: [int(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]
readarrs = lambda: [str(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]

mod = 998244353
MOD = int(1e9) + 7
N = int(5e5) + 2
fNI, nNI, fact = [0 for _ in range(N + 1)], [0 for _ in range(N + 1)], [0 for _ in range(N + 1)]
adj, visited, ways, st, a = list(), list(), list(), list(), list()
n = None

sys.setrecursionlimit(int(1e6) + 69)


def reset_global():
    global adj, visited, ways, st, n, a
    adj = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    ways = [0 for _ in range(n)]
    st = [0 for _ in range(n)]
    a = list()


def check_possible(parent):
    global a, adj, visited, st, n
    visited[parent], ans = 1, 0
    for i in adj[parent]:
        if(not(visited[i])):
            curr = check_possible(i)
            a.append([min(curr, n - curr), [i, parent]])
            ans += curr
    ans += 1; st[parent] = ans
    return ans


def add(val1, val2):
    return (val1 % MOD + val2 % MOD) % MOD


def mult(val1, val2):
    return (val1 % MOD * val2 % MOD) % MOD


def IoN():
    nNI[0] = nNI[1] = 1
    for i in range(2, N + 1): nNI[i] = (nNI[MOD % i] * (MOD - MOD // i) % MOD)


def IoF():
    fNI[0] = fNI[1] = 1
    for i in range(2, N + 1): fNI[i] = (nNI[i] * fNI[i - 1]) % MOD


def f():
    fact[0] = 1
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % MOD


def bino(nn, rr):
    return ((fact[nn] * fNI[rr]) % MOD * fNI[nn - rr]) % MOD


def tryy():
    check_possible(0)


def search(parent):
    global adj, visited, ways
    visited[parent], ans, family = 1, 1, 0
    for i in adj[parent]:
        if(not(visited[i])):
            child = search(i)
            ans = mult(ans, ways[i])
            ans = mult(ans, bino(family + child, child))
            family += child
    ways[parent] = ans; family += 1
    return family


def solve():
    global visited, adj, ways, st, n
    n, k = readints()
    reset_global()
    for _ in range(n - 1):
        x, y = readints()
        adj[x - 1].append(y - 1)
        adj[y - 1].append(x - 1)
    # Corner Case, handle n = 1 alone
    if(n == 1):
        search(0)
        print(1, ways[0])
        return
    tryy()
    visited = [0 for _ in range(n)]
    a.sort(reverse=True)
    ans1, ans2 = 0, 0
    if(a[0][0] == a[1][0]):
        if(a[0][1][0] != a[1][1][0] and a[0][1][0] != a[1][1][1]): ans1 = a[0][1][1]
        else: ans1 = a[0][1][0]
        iter = 1
        if(a[0][1][0] != ans1): ans2 = max(a[0][1][0], ans2)
        else: ans2 = max(a[0][1][1], ans2)
        la = len(a)
        while(a[iter - 1][0] == a[iter][0] and iter != n):
            if(a[iter][1][0] == ans1): ans2 = max(ans2, a[iter][1][1])
            else: ans2 = max(ans2, a[iter][1][0])
            iter += 1
            if(iter == la): break
    else:
        if(st[a[0][1][0]] != n - st[a[0][1][0]]):
            if (st[a[0][1][0]] > n - st[a[0][1][0]]): ans1 = a[0][1][0]; ans2 = a[0][1][1]
            else: ans2 = a[0][1][0]; ans1 = a[0][1][1]
        else:
            ans1 = max(a[0][1][0], a[0][1][1])
            ans2 = min(a[0][1][0], a[0][1][1])
    if(k == 1): search(ans1)
    else: search(ans2)
    print(" ".join([str(ans1 + 1), str((ways[ans1] + MOD) % MOD)]) if(k == 1) else " ".join([str(ans2 + 1), str((ways[ans2] + MOD) % MOD)]))


def main():
    # orig_stdin = sys.stdin
    # orig_stdout = sys.stdout
    # f1 = open("D:\\n1\\New folder\\cp\\in.txt", 'r')
    # f2 = open("D:\\n1\\New folder\\cp\\out.txt", 'w')
    # sys.stdin = f1
    # sys.stdout = f2
    IoN()
    IoF()
    f()
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()
    # sys.stdin = orig_stdin
    # sys.stdout = orig_stdout
    # f1.close()
    # f2.close()


if __name__ == "__main__":
    main()
