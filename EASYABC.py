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


def solve():
    s = readstr()
    posi = defaultdict(list)
    a, b, c = 0, 0, 0
    for i in range(len(s)):
        if(s[i] == 'a'): a = 1
        if(s[i] == 'b'): b = 1
        if(s[i] == 'c'): c = 1
        posi[s[i]].append(i)
    v1 = v2 = v3 = v4 = v5 = v6 = -int(1e6) + 1
    if(a and b):
        mina = min(posi['a']); minb = min(posi['b'])
        maxa = max(posi['a']); maxb = max(posi['b'])
        v1 = abs(mina - maxb)
        v3 = abs(minb - maxa)
    if(c):
        minc = min(posi['c']); maxc = max(posi['c'])
        if(a):
            v2 = abs(mina - maxc)
            v5 = abs(minc - mina)
        if(b):
            v4 = abs(minb - maxc)
            v6 = abs(minc - minb)
    print(max(v1, v2, v3, v4, v5, v6))


def main():
    t = 1
    # t = readint()
    for _ in range(t):
        # print("Case #" + str(_) +": ")
        solve()


if __name__ == "__main__":
    main()
