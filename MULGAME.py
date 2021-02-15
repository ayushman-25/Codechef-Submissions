'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
from collections import defaultdict
from itertools import accumulate
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
check_arr, mymap, queries = [0 for _ in range(int(1e5) + 69)], defaultdict(int), set()


def ans(m):
    games_won = 0
    for i in range(1, m + 1):
        check_arr[i] += check_arr[i - 1]
        games_won = max(games_won, check_arr[i])
    print(games_won)


def clear_global():
    global check_arr, mymap, queries
    check_arr = [0 for _ in range(int(1e5) + 69)]
    mymap = defaultdict(int)
    queries = set()


def checks(l, r, m, arr):
    global check_arr, mymap
    check_arr[arr[l]] += 1
    check_arr[m + 1] -= 1
    if (arr[r] <= m): queries.add((arr[l], arr[r])); mymap[(arr[l], arr[r])] += 1
    elif (arr[r] > m and arr[l] <= m): pass
    else: assert(False)


def find_eff(m):
    global check_arr, mymap
    for z in queries:
        val = z[1] + (z[0] << 1)
        check_arr[z[1] + z[0]] -= mymap[z]
        check_arr[z[1] + (z[0] << 1)] += mymap[z]
        while (val + z[1] <= m):
            check_arr[val + z[0] + z[1]] += mymap[z]
            check_arr[val + z[1]] -= mymap[z]
            val += z[0] + z[1]


def solve():
    n, q, m = readints()
    arr = readarri()
    for _ in range(q):
        l, r = readints()
        if (arr[l - 1] > m): continue
        checks(l - 1, r - 1, m, arr)
    # solving queries offline for more efficient approach
    find_eff(m)
    # print(max(accumulate(check_arr)))
    ans(m)
    clear_global()


def main():
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
