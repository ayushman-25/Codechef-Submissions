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


def solve():
    n, m = readints()
    mat = [list(readstr()) for _ in range(n)]
    # print(mat)
    f1, f2, f3, f4 = [], [], [], []
    cnt1s = 0
    for i in range(n):
        for j in range(m):
            cnt1s += int(mat[i][j])
    for i in range(n):
        for j in range(m):
            if(mat[i][j] == '1'):
                f1.append(i)
                f1.append(j)
                break
        if(f1):
            break
    if not(f1):
        print("NO")
        return
    for i in range(m):
        if(mat[f1[0]][m - i - 1] == '1'):
            f2.append(f1[0])
            f2.append(m - i - 1)
            break
    if not(f2):
        print("NO")
        return
    for i in range(n):
        for j in range(m):
            if(mat[n - i - 1][j] == '1'):
                f3.append(n - i - 1)
                f3.append(j)
                break
        if(f3):
            break
    if not(f3):
        print("NO")
        return
    for i in range(m):
        if(mat[f3[0]][m - i - 1] == '1'):
            f4.append(f3[0])
            f4.append(m - i - 1)
            break
    if not(f4):
        print("NO")
        return
    # print(f1, f2, f3, f4)
    c1, c0 = 0, 0
    for i in range(f1[0], f3[0] + 1):
        for j in range(f1[1], f2[1] + 1):
            # print(i, j)
            if(mat[i][j] == '0'): c0 += 1
            elif(mat[i][j] == '1'): c1 += 1
    # print(f1, f2, f3, f4)
    # print(c1, c0)
    print("YES" if (c1 == cnt1s and c0 == 0) else "NO")


def main():
    # orig_stdout = sys.stdout
    # f = open("D:\\n1\\New folder\\cp\\out.txt", 'w')
    # sys.stdout = f
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()
    # sys.stdout = orig_stdout
    # f.close()


if __name__ == "__main__":
    main()
