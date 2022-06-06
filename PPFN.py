'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
# from collections import *
from itertools import permutations
from math import floor, sqrt
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


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
readint = lambda: int(sys.stdin.readline().rstrip("\r\n"))
readints = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split())
readstr = lambda: sys.stdin.readline().rstrip("\r\n")
readstrs = lambda: map(str, sys.stdin.readline().rstrip("\r\n").split())
readarri = lambda: [int(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]
readarrs = lambda: [str(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]


def sie(lim, primes):
    mark = [0] * (lim + 1)
    for i in range(2, lim + 1):
        if(not mark[i]):
            primes.append(i)
            for j in range(i, lim + 1, i):
                mark[j] = True


def rangee(l, r):
    lim = floor(sqrt(r)) + 1
    primes = []
    sie(lim, primes)
    n = r - l + 1
    mark = [0] * (n + 1)
    for i in range(len(primes)):
        loLim = floor(l / primes[i]) * primes[i]
        if loLim < l: loLim += primes[i]
        if loLim == primes[i]: loLim += primes[i]
        for j in range(loLim, r + 1, primes[i]):
            if j != primes[i]: mark[j - l] = True
    L = []
    for i in range(l, r + 1):
        if(not mark[i - l] and i != 1):
            L.append(i)
    return L


def cP(inp, b, isOdd):
    n = inp
    palin = inp
    if (isOdd):
        n = n / b
    while (n > 0):
        palin = palin * b + (n % b)
        n = n / b
    return palin


def solve():
    s = readstr()
    ans = set()
    maxV = int("".join(sorted(s, reverse=True)))
    print(maxV)
    palin = list()
    for j in range(2):
        i = 1
        while(cP(i, 10, j & 1) < maxV):
            palin.append(cP(i, 10, j & 1))
            i += 1
    for i in palin:
        print(i)


    if(not(ans)):
        print(-1)
        return
    print(*sorted(ans))


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
