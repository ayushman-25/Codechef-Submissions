'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
from collections import defaultdict
# from itertools import *
from math import ceil
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
dy = [0, 1, 0, -1]


def solve():
    a, b = readints()
    arr = [readstr() for _ in range(a)]
    adj, vertices, start, idd = [set() for _ in range(a * b)], [[]], 0, defaultdict(tuple)
    for i in range(a):
        for j in range(b):
            idd[start] = (i, j)
            vertices[-1].append(start)
            start += 1
        vertices.append([])
    for i in range(a):
        for j in range(b):
            if(arr[i][j] == '1'):
                for k in range(4):
                    c1 = i + dx[k]
                    c2 = j + dy[k]
                    if(0 <= c1 <= a - 1 and 0 <= c2 <= b - 1):
                        if(arr[c1][c2] == '1'):
                            adj[vertices[i][j]].add(vertices[c1][c2])
                            adj[vertices[c1][c2]].add(vertices[i][j])
    ncc, vis = list(), [0 for _ in range(a * b)]
    vis = [0 for _ in range(a * b)]
    for i in range(a * b):
        if(arr[idd[i][0]][idd[i][1]] == '1'):
            if(not vis[i]):
                temp, qu, vis[i] = [i], [i], 1
                while(qu):
                    par = qu.pop(0)
                    for j in adj[par]:
                        if(not vis[j]):
                            temp.append(j)
                            qu.append(j)
                            vis[j] = 1
                ncc.append(temp)
    ncc = sorted([len(i) for i in ncc], reverse=True)
    print(sum(ncc[i] for i in range(1, len(ncc), 2)))


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
