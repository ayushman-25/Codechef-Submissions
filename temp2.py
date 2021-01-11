'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
import random
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


def getSum(BITTree, i):
    s = 0
    i = i + 1
    while(i > 0):
        s += BITTree[i]
        i -= i & (-i)
    return s


def update(BITTree, n, i, v):
    i += 1
    while(i <= n):
        BITTree[i] += v
        i += (i & (-i))


def construct(arr, n):
    BITTree = [0] * (n + 1)
    for i in range(n):
        update(BITTree, n, i, arr[i])
    return BITTree


def check(curr, n, k, smallK):
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]
    if (n == 1): return 0
    for i in range(n): dp[i][0] = 1
    for i in range(1, n):
        for z in range(1, k + 1):
            if (z >= curr[i]): dp[i][z] = (dp[i - 1][z] or dp[i - 1][z - curr[i]])
            else: dp[i][z] = dp[i - 1][z]
            if (smallK <= z <= k and dp[i][z]): return 1
    return 0


def solve():
    n, x, y = readints()
    arr = readarri()
    if (n == 1):
        if (x <= arr[0] <= y): print(0)
        else: print(-1)
        return
    startsum = 0
    for i in range(n):
        if (x <= startsum <= y):
            print(0)
            return
        startsum += arr[i]
        if (i == n - 1):
            if (x <= startsum <= y):
                print(0)
                return
    if (not (check(sorted(arr), n, y, x))):
        print(-1)
        return
    BITTree = construct(arr, n)
    for i in range(n):
        for j in range(i + 1, n):
            val1 = arr[i]
            val2 = arr[j]
            update(BITTree, n, i, -arr[i] + val2)
            update(BITTree, n, j, -arr[j] + val1)
            l, r = 0, n - 1
            while(l <= r):
                mid = l + (r - l) // 2
                tSum = getSum(BITTree, mid)
                if(x <= tSum <= y): print(1); return
                elif(tSum < x): l = mid + 1
                else: r = mid - 1
            update(BITTree, n, i, -val2 + val1)
            update(BITTree, n, j, -val1 + val2)
    print(2)


def main():
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_) +": ")
        solve()


if __name__ == "__main__":
    main()
