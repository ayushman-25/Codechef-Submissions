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

ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def isReachable(a, b, adj):
    visited = [0] * len(adj)
    qu = [a]
    visited[a] = 1
    while(qu):
        h = qu.pop(0)
        if(h == b):
            return True
        for i in adj[h]:
            if(not(visited[i])):
                qu.append(i)
                visited[i] = 1
    return False


def solve():
    while(1):
        a, b = readints()
        if(a == b == 0):
            return
        mat = [readstr() for _ in range(a)]
        adj = [set() for _ in range(a * b)]
        vertices = [[]]
        start = 0
        for i in range(a):
            for j in range(b):
                vertices[-1].append(start)
                start += 1
            vertices.append([])
        vertices = vertices[:-1]
        if (a == b == 1):
            if (mat[0][0] == 'A'): print(1)
            else: print(0)
            continue
        if(a == 1):
            if('A' not in mat[0]):
                print(0)
                continue
            for i in range(b):
                if(mat[0][i] != 'Z'):
                    curr = mat[0][i]
                    to = ALP[ALP.index(curr) + 1]
                    if(i == 0):
                        if (mat[0][i + 1] == to): adj[vertices[0][i]].add(vertices[0][i + 1])
                    elif(i == b - 1):
                        if (mat[0][i - 1] == to): adj[vertices[0][i]].add(vertices[0][i - 1])
                    else:
                        if (mat[0][i + 1] == to): adj[vertices[0][i]].add(vertices[0][i + 1])
                        if (mat[0][i - 1] == to): adj[vertices[0][i]].add(vertices[0][i - 1])
        elif(b == 1):
            if('A' not in [mat[i][0] for i in range(a)]):
                print(0)
                continue
            for i in range(a):
                if(mat[i][0] != 'Z'):
                    curr = mat[i][0]
                    to = ALP[ALP.index(curr) + 1]
                    if (i == 0):
                        if (mat[i + 1][0] == to): adj[vertices[i][0]].add(vertices[i + 1][0])
                    elif (i == a - 1):
                        if (mat[i - 1][0] == to): adj[vertices[i][0]].add(vertices[i - 1][0])
                    else:
                        if (mat[i + 1][0] == to): adj[vertices[i][0]].add(vertices[i + 1][0])
                        if (mat[i - 1][0] == to): adj[vertices[i][0]].add(vertices[i + 1][0])
        else:
            for i in range(a):
                for j in range(b):
                    if (mat[i][j] != 'Z'):
                        curr = mat[i][j]
                        to = ALP[ALP.index(curr) + 1]
                        if (i == 0):
                            if (j == 0):
                                if (mat[i][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j + 1])
                                if (mat[i + 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j])
                                if (mat[i + 1][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j + 1])
                            elif (j == b - 1):
                                if (mat[i][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j - 1])
                                if (mat[i + 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j])
                                if (mat[i + 1][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j - 1])
                            else:
                                if (mat[i][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j - 1])
                                if (mat[i][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j + 1])
                                if (mat[i + 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j])
                                if (mat[i + 1][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j - 1])
                                if (mat[i + 1][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j + 1])
                        elif (i == a - 1):
                            if (j == 0):
                                if (mat[i][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j + 1])
                                if (mat[i - 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j])
                                if (mat[i - 1][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j + 1])
                            elif (j == b - 1):
                                if (mat[i][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j - 1])
                                if (mat[i - 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j])
                                if (mat[i - 1][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j - 1])
                            else:
                                if (mat[i][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j - 1])
                                if (mat[i][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j + 1])
                                if (mat[i - 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j])
                                if (mat[i - 1][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j - 1])
                                if (mat[i - 1][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j + 1])
                        else:
                            if (j == 0):
                                if (mat[i][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j + 1])
                                if (mat[i - 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j])
                                if (mat[i + 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j])
                                if (mat[i - 1][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j + 1])
                                if (mat[i + 1][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j + 1])
                            elif (j == b - 1):
                                if (mat[i][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j - 1])
                                if (mat[i - 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j])
                                if (mat[i + 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j])
                                if (mat[i - 1][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j - 1])
                                if (mat[i + 1][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j - 1])
                            else:
                                if (mat[i][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j + 1])
                                if (mat[i][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i][j - 1])
                                if (mat[i - 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j])
                                if (mat[i + 1][j] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j])
                                if (mat[i - 1][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j + 1])
                                if (mat[i + 1][j + 1] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j + 1])
                                if (mat[i - 1][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i - 1][j - 1])
                                if (mat[i + 1][j - 1] == to):
                                    adj[vertices[i][j]].add(vertices[i + 1][j - 1])
        ans = 1
        A = [vertices[i][j] for i in range(a) for j in range(b) if(mat[i][j] == 'A')]
        for i in range(1, 26):
            to = [vertices[k][j] for k in range(a) for j in range(b) if(mat[k][j] == ALP[i])]
            for k in A:
                for m in to:
                    if(isReachable(k, m, adj)):
                        ans = max(ans, i + 1)
        print(ans)


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
