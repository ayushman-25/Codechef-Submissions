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


def recur(c, b, a, h, e, n):
    ans = int(1e18) + 69
    if (2 * n <= e): ans = min(ans, n * a)
    if (3 * n <= h): ans = min(ans, n * b)
    if (n <= e and n <= h): ans = min(ans, n * c)
    if (((h - n) >> 1) >= (n - e) and ((h - n) >> 1) >= 1):
        if (b >= c): ans = min(ans, max(n - e, 1) * (b - c) + n * c)
        else: ans = min(ans, min(n - 1, ((h - n) >> 1)) * (b - c) + n * c)
    if ((e >> 1) >= (3 * n - h + 2) // 3 and (e >> 1) >= 1):
        if (a >= b): ans = min(ans, max((3 * n - h + 2) // 3, 1) * (a - b) + n * b)
        else:  ans = min(ans, min(n - 1, (e >> 1)) * (a - b) + n * b)
    if ((e + h) >= (n << 1) and (e - n) >= 1):
        if (a >= c): ans = min(ans, max(1, n - h) * (a - c) + n * c)
        else: ans = min(ans, min(n - 1, e - n) * (a - c) + n * c)
    if (n >= 3 and e >= 3 and h >= 4):
        ans = min(ans, a + b + c + recur(c, b, a, h - 4, e - 3, n - 3))
    return ans


def solve():
    n, e, h, a, b, c = readints()
    mini = min(e, h) + ((e - min(e, h)) // 2) + ((h - min(e, h)) // 3)
    if (mini < n):
        print(-1)
        return
    result = recur(c, b, a, h, e, n)
    assert (result != (int(1e18) + 69))
    print(result)


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
