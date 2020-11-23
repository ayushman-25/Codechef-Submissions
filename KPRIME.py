'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
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


n = 100000
prime = [True] * (n + 1)
ans = [0] * (n + 1)


def seive():
    p = 2
    while(p * p <= n):
        if(prime[p]):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1


def pf():
    for N in range(2, n + 1):
        prim = []
        curr = N
        while(N % 2 == 0):
            prim.append(2)
            N /= 2
        for i in range(3, int(n ** (1 / 2)) + 1, 2):
            while(N % i == 0):
                prim.append(i)
                N /= i
        if(N > 2):
            prim.append(n)
        for i in set(prim):
            if(prime[i]):
                ans[curr] += 1


def solve():
    a, b, k = readints()
    anss = 0
    # print(ans)
    for i in range(a, b + 1):
        if(ans[i] == k):
            anss += 1
    print(anss)


def main():
    seive()
    pf()
    # print(prime)
    for _ in range(readint()):
        solve()


if __name__ == "__main__":
    main()
