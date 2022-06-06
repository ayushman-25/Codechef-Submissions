'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
from collections import defaultdict
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


dx = [-1, 0, 1, 0]
dy = dx[::-1]


def solve():
    n, m = readints()
    mat = [readarri() for _ in range(n)]
    x1, y1, x2, y2 = readints()
    vertices = defaultdict(int)
    v = 0
    for i in range(n):
        for j in range(m):
            vertices[(i, j)] = v
            v += 1
    src = vertices[(x1, y1)]
    des = vertices[(x2, y2)]
    adj = [set() for _ in range(n * m)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if(0 <= i + dx[k] < n and  0 <= j + dy[k] < m):
                    if(mat[i + dx[k]][j + dy[k]] == mat[x1][y1] == mat[i][j]):
                        adj[vertices[(i + dx[k], j + dy[k])]].add(vertices[(i, j)])
                        adj[vertices[(i, j)]].add(vertices[(i + dx[k], j + dy[k])])
    vis = [0 for _ in range(n * m)]
    vis[src] = 1
    qu = [src]
    distances = [0 for _ in range(n * m)]
    while(qu):
        par = qu.pop(0)
        if(par == des):
            print(distances[des])
            return
        for i in adj[par]:
            if(not vis[i]):
                qu.append(i)
                distances[i] = distances[par] + 1
                vis[i] = 1
    print(-1)


def main():
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
