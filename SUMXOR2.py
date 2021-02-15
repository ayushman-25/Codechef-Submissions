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
N = int(2e5) + 2
fNI, nNI, fact = [0 for _ in range(N + 1)], [0 for _ in range(N + 1)], [0 for _ in range(N + 1)]


def add(val1, val2):
    return (val1 % mod + val2 % mod) % mod


def mult(val1, val2):
    return (val1 % mod * val2 % mod) % mod


def IoN():
    nNI[0] = nNI[1] = 1
    for i in range(2, N + 1): nNI[i] = (nNI[mod % i] * (mod - mod // i) % mod)


def IoF():
    fNI[0] = fNI[1] = 1
    for i in range(2, N + 1): fNI[i] = (nNI[i] * fNI[i - 1]) % mod


def f():
    fact[0] = 1
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % mod


def bino(nn, rr):
    return ((fact[nn] * fNI[rr]) % mod * fNI[nn - rr]) % mod


def solve():
    n = readint()
    arr = readarri()
    mat = [[0 for _ in range(32)] for _ in range(n)]
    for i in range(n):
        start = 31
        while(arr[i]):
            mat[i][start] = arr[i] & 1
            arr[i] >>= 1
            start -= 1
    cnt_1 = [sum(mat[j][_] for j in range(n)) for _ in range(32)]
    pre = [0 for _ in range(n + 1)]
    for k in range(1, n + 1):
        ans = 0
        for i in range(1, k + 1, 2):
            for j in range(31, -1, -1):
                if (cnt_1[j] < i or (n - cnt_1[j]) < (k - i)): continue
                temp = mult(bino((n - cnt_1[j]), (k - i)), bino(cnt_1[j], i))
                temp = mult(temp, 1 << (31 - j))
                ans = add(ans, temp)
        pre[k] = add(pre[k - 1], ans)
    for _ in range(readint()): print(pre[readint()])


def main():
    IoN()
    IoF()
    f()
    t = 1
    # t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
