'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
# from collections import *
# from itertools import *
from math import log2, ceil
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

sys.setrecursionlimit(int(1e6) + 69)
n = l = timer = None
adj, up, tin, tout = list(), list(), list(), list()


def dfs(v, p):
    global tin, up, tout, timer
    timer += 1
    tin[v] = timer
    up[v][0] = p
    for i in range(1, l + 1):
        up[v][i] = up[up[v][i - 1]][i - 1]
    for i in adj[v]:
        if (i != p):
            dfs(i, v)
    timer += 1
    tout[v] = timer


def is_ancestor(u, v):
    global tin, tout
    return tin[u] <= tin[v] and tout[u] >= tout[v]


def lca(u, v):
    global l, up
    if (is_ancestor(u, v)): return u
    if (is_ancestor(v, u)): return v
    for i in range(l, -1, -1):
        if (not is_ancestor(up[u][i], v)):
            u = up[u][i]
    return up[u][0]


def preprocess(root):
    global tin, tout, timer, l, up, n
    tin = [0] * n
    tout = [0] * n
    timer = 0
    l = ceil(log2(n))
    up = [[0 for _ in range(l + 1)] for _ in range(n)]
    dfs(root, root)


def solve():
    global n, adj
    n = readint()
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        l, r = readints()
        l -= 1;
        r -= 1
        adj[l].append(r)
        adj[r].append(l)
    preprocess(0)
    for _ in range(readint()):
        root, u, v = readints()
        root -= 1;
        u -= 1;
        v -= 1
        uv, ur, vr = lca(u, v), lca(u, root), lca(v, root)
        if (uv == ur):
            print(vr + 1)
        elif (ur == vr):
            print(uv + 1)
        elif (uv == vr):
            print(ur + 1)
        else:
            assert (False)


def main():
    t = 1
    # t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
