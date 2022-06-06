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


def solve():
    n, m, e = readints()
    # Considering just the checkerboard pattern
    mat_a = [[int(i) for i in readstr()] for _ in range(n)]
    mat_b = [[int(i) for i in readstr()] for _ in range(n)]
    if(mat_a == mat_b):
        print(0); return
    # Now checking if b is just 0 matrix
    assert (all(mat_b[i][j] == 0 for i in range(n) for j in range(m)))
    cnt_one = 0
    for i in range(n):
        for j in range(m):
            cnt_one += (mat_a[i][j] == 1)
    # now if a 2 x 2 matrix OR odd ones, then not possible...
    if(n == m == 2 or cnt_one & 1):
        print(-1); return
    print(cnt_one >> 1)
    if(e):
        for i in range(1, n + 1):
            j = 1
            while(True):
                if(j >= m - 1): break
                if(mat_a[i - 1][j - 1] and mat_a[i - 1][j + 1]):
                    print('R', i, j, j + 2)
                    j += (1 << 2)
                    continue
                j += 1
        for i in range(1, n + 1):
            j = 1
            while(True):
                if(j >= m - 1): break
                change = (mat_a[i - 1][j - 1] and mat_a[i - 1][j + 1])
                mat_a[i - 1][j - 1] ^= change
                mat_a[i - 1][j + 1] = mat_a[i - 1][j - 1]
                if(change):
                    j += (1 << 2)
                    continue
                j += 1
        for i in range(1, m + 1):
            j = 1
            while(True):
                if(j >= n - 1): break
                if(mat_a[j - 1][i - 1] and mat_a[j + 1][i - 1]):
                    print('C', i, j, j + 2)
                    j += (1 << 2)
                    continue
                j += 1


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