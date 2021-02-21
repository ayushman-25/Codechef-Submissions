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
    a, x, y, z = readints()
    X, Y, Z = readarri(), readarri(), readarri()
    X.sort()
    Y.sort()
    Z.sort()
    if((X[0] + Y[0] + Z[0]) > a):
        print(-1)
        return
    ans = 0
    for i in range(x):
        for j in range(y):
            curr_sum = X[i] + Y[j]
            # now binary search
            left, right = 0, z - 1
            while(left <= right):
                middle = left + (right - left) // 2
                if(curr_sum + Z[middle] > a):
                    right = middle - 1
                elif(curr_sum + Z[middle] < a):
                    left = middle + 1
                    ans = max(ans, curr_sum + Z[middle])
                else:
                    ans = max(ans, curr_sum + Z[middle])
                    break
    for i in range(y):
        for j in range(z):
            curr_sum = Y[i] + Z[j]
            # now binary search
            left, right = 0, x - 1
            while(left <= right):
                middle = left + (right - left) // 2
                if(curr_sum + X[middle] > a):
                    right = middle - 1
                elif(curr_sum + X[middle] < a):
                    left = middle + 1
                    ans = max(ans, curr_sum + X[middle])
                else:
                    ans = max(ans, curr_sum + X[middle])
                    break
    for i in range(x):
        for j in range(z):
            curr_sum = X[i] + Z[j]
            # now binary search
            left, right = 0, y - 1
            while(left <= right):
                middle = left + (right - left) // 2
                if(curr_sum + Y[middle] > a):
                    right = middle - 1
                elif(curr_sum + Y[middle] < a):
                    left = middle + 1
                    ans = max(ans, curr_sum + Y[middle])
                else:
                    ans = max(ans, curr_sum + Y[middle])
                    break
    print(a - ans)


def main():
    t = 1
    # t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
