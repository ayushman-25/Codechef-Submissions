'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
from heapq import *
# from queue import PriorityQueue
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
    # N = 2 * int(1e5) + 5
    n, k, b, c = readints()
    a = readarri()
    for i in range(n):
        a[i] += int(1e9)
    a.sort()
    a.reverse()
    ans = (1 << 60)
    if(5 * c <= b):
        sum = 0
        for i in range(k - 1):
            sum += a[i]
        for i in range(n - k + 1):
            sum += a[i + k - 1]
            ans = min(ans, (a[i] * k - sum) * c)
            sum -= a[i]
    else:
        a.reverse()
        for m in range(5):
            sum = 0
            heap = []
            heapify(heap)
            for i in range(n):
                bb = a[i]
                d = (m + 5 - a[i] % 5) % 5
                bb = (bb + d) // 5
                cc = d * c - bb * b
                heappush(heap, -cc)
                sum += cc
                while(len(heap) > k):
                    sum -= -(heappop(heap))
                if(len(heap) == k):
                    ans = min(ans, sum + k * bb * b)
    print(ans)


def main():
    # for _ in range(readint()):
    solve()


if __name__ == "__main__":
    main()
