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


right = 131072
size = 255005
K = [0] * size
D = [0] * size
LK = [0] * size
LD = [0] * size
S = [0] * size


def q(l, r, n=1, a=1, b=right):
    if(a > r or b < l): return 0
    if(a >= l and b <= r): return S[n]
    if(LK[n] != 0 or LD[n] != 0):
        sz = (b - a + 1) // 2
        K[2 * n] += LK[n]
        K[2 * n + 1] += LK[n] + LD[n] * sz
        D[2 * n] += LD[n]
        D[2 * n + 1] += LD[n]
        S[2 * n] += LK[n] * sz + LD[n] * sz * (sz - 1) // 2
        S[2 * n + 1] += (LK[n] + LD[n] * sz) * sz + LD[n] * sz * (sz - 1) // 2
        LK[2 * n] += LK[n]
        LK[2 * n + 1] += LK[n] + LD[n] * sz
        LD[2 * n] += LD[n]
        LD[2 * n + 1] += LD[n]
        LK[n] = LD[n] = 0
    mid = (a + b) // 2
    return q(l, r, 2 * n, a, mid) + q(l, r, 2 * n + 1, mid + 1, b)


def u(l, r, k, d, n=1, a=1, b=right):
    if(a >= l and b <= r):
        K[n] += k
        D[n] += d
        LK[n] += k
        LD[n] += d
        S[n] += (k * (b - a + 1)) + d * (b - a + 1) * ((b - a + 1) - 1) // 2
        return
    if(LK[n] != 0 or LD[n] != 0):
        sz = (b - a + 1) // 2
        K[2 * n] += LK[n]
        K[2 * n + 1] += LK[n] + LD[n] * sz
        D[2 * n] += LD[n]
        D[2 * n + 1] += LD[n]
        S[2 * n] += LK[n] * sz + LD[n] * sz * (sz - 1) // 2
        S[2 * n + 1] += (LK[n] + LD[n] * sz) * sz + LD[n] * sz * (sz - 1) // 2
        LK[2 * n] += LK[n]
        LK[2 * n + 1] += LK[n] + LD[n] * sz
        LD[2 * n] += LD[n]
        LD[2 * n + 1] += LD[n]
        LK[n] = LD[n] = 0
    mid = (a + b) // 2
    if(l <= mid): u(l, min(mid, r), k, d, 2 * n, a, mid)
    if(r > mid): u(max(mid + 1, l), r, k + d * max(mid - l + 1, 0), d, 2 * n + 1, mid + 1, b)
    S[n] = S[2 * n] + S[2 * n + 1]


def reset():
    global K, D, LK, LD, S
    K = [0] * size
    D = [0] * size
    LK = [0] * size
    LD = [0] * size
    S = [0] * size


def solve():
    n, qu = readints()
    for _ in range(qu):
        a, b = readints()
        u(a, b, 1, 1)
    for i in range(1, n + 1):
        print(q(i, i), end=' ')
    print()
    reset()


def main():
    t = 1
    t = readint()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
