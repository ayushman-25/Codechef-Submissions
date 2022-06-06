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


# REFERENCES - CPALGORITHMS (nlogn precompute LCA using bin lifting)


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
        if(i != p):
            dfs(i, v)
    timer += 1
    tout[v] = timer


def is_ancestor(u, v):
    global tin, tout
    return tin[u] <= tin[v] and tout[u] >= tout[v]


def lca(u, v):
    global l, up
    if(is_ancestor(u, v)): return u
    if(is_ancestor(v, u)): return v
    for i in range(l, -1, -1):
        if(not is_ancestor(up[u][i], v)):
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
    n, q = readints()
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = readints()
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    preprocess(0)
    myDepths = [0] * n
    vis = [0] * n
    vis[0] = 1
    qu = [0]
    while(qu):
        par = qu.pop(0)
        for i in adj[par]:
            if(not vis[i]):
                myDepths[i] = myDepths[par] + 1
                qu.append(i)
                vis[i] = 1
    for _ in range(q):
        a, b = readints()
        a -= 1; b -= 1
        print(sum(min(myDepths[i] + myDepths[a] - ((myDepths[lca(i, a)]) << 1), myDepths[i] + myDepths[b] - ((myDepths[lca(i, b)]) << 1)) for i in range(n)))
    adj.clear()


def main():
    # orig_stdin = sys.stdin
    # orig_stdout = sys.stdout
    # f1 = open("D:\\n1\\New folder\\cp\\in.txt", 'r')
    # f2 = open("D:\\n1\\New folder\\cp\\out.txt", 'w')
    # sys.stdin = f1
    # sys.stdout = f2
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
