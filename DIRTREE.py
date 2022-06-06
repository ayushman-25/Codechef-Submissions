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


sys.setrecursionlimit(int(1e6) + 69)
height, euler, first, segtree, visited = [], [], [], [], []
n = None


def dfs(adj, node, h=0):
    global visited, height, euler
    visited[node] = 1
    height[node] = h
    first[node] = len(euler)
    euler.append(node)
    for i in adj[node]:
        if(not (visited[i])):
            dfs(adj, i, h + 1)
            euler.append(node)


def build(node, b, e):
    global segtree, euler, height
    if (b == e): segtree[node] = euler[b]
    else:
        mid = (b + e) >> 1
        build(node << 1, b, mid)
        build(node << 1 | 1, mid + 1, e)
        l = segtree[node << 1]
        r = segtree[node << 1 | 1]
        segtree[node] = l if (height[l] < height[r]) else r


def query(node, b, e, L, R):
    global segtree, height
    if (b > R or e < L): return -1
    if (b >= L and e <= R): return segtree[node]
    mid = (b + e) >> 1
    left = query(node << 1, b, mid, L, R)
    right = query(node << 1 | 1, mid + 1, e, L, R)
    if (left == -1): return right
    if (right == -1): return left
    return left if (height[left] < height[right]) else right


def preC(adj, root=0):
    global height, euler, first, segtree, visited, n
    n = len(adj)
    height = [0 for _ in range(n)]
    first = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    dfs(adj, root)
    m = len(euler)
    segtree = [0 for _ in range(m * 4)]
    build(1, 0, m - 1)


def lca(u, v):
    global first, euler, height
    left, right = first[u], first[v]
    right = first[v]
    if (left > right): left, right = right, left
    if (height[u] < height[v] and query(1, 0, len(euler) - 1, left, right) == u):
        return 1
    return 0



def solve():
    n, q = readints()
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = readints()
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    preC(adj)
    for _ in range(q):
        a, b = readints()
        print("YES" if(lca(a - 1, b - 1)) else "NO")


def main():
    # orig_stdin = sys.stdin
    # orig_stdout = sys.stdout
    # f1 = open("D:\\n1\\New folder\\cp\\in.txt", 'r')
    # f2 = open("D:\\n1\\New folder\\cp\\out.txt", 'w')
    # sys.stdin = f1
    # sys.stdout = f2
    t = 1
    # t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()
    # sys.stdin = orig_stdin
    # sys.stdout = orig_stdout
    # f1.close()
    # f2.close()


if __name__ == "__main__":
    main()
