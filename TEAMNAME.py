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

mod = 998244353
MOD = int(1e9) + 7
alp = 'abcdefghijklmnopqrstuvwxyz'


def solve():
    n = readint()
    arr = readarrs()
    funny, pre_store, ls = defaultdict(str), defaultdict(list), defaultdict(int)
    for i in arr:
        pre_store[i[1:]].append(i[0])
        funny[i] = 1
    ps, lp = list(pre_store.keys()), len(pre_store)
    for i in range(lp):
        for j in range(i + 1, lp):
            ls[(i, j)] = len(set(pre_store[ps[i]] + pre_store[ps[j]]))
    ans = 0
    pre_cut, tc = [i[1:] for i in arr], [[] for _ in range(26)]
    for _ in range(26):
        for i in pre_cut:
            tc[_].append(alp[_] + i)
    if(n <= 2e3):
        for i in range(n):
            for j in range(i + 1, n):
                if(not(funny[tc[ord(arr[j][0]) - 97][i]]) and not(funny[tc[ord(arr[i][0]) - 97][j]])):
                    ans += 2
        print(ans)
    else:
        for i in range(lp):
            for j in range(i + 1, lp):
                ans += ((ls[(i, j)] - len(pre_store[ps[i]])) * (ls[(i, j)] - len(pre_store[ps[j]]))) << 1
        print(ans)


def main():
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
