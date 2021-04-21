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


def solve():
    s = readstr()
    if all(int(i) for i in s):
        print(0)
        return
    n = len(s)
    start = 0
    if (n <= 10):
        while (1):
            bins = bin(start).replace('0b', '')
            bs = len(bins)
            got_it = 0
            for i in range(n):
                if (s[i] == bins[got_it]): got_it += 1
                if (got_it == bs): break
            if (got_it < len(bins)):
                print(bins)
                return
            start += 1
    else:
        if(all(not(int(i)) for i in s)): print(1); return
        dp0, dp1 = [0 for _ in range(n + 69)], [0 for _ in range(n + 69)]
        nx0, nx1 = [None for _ in range(n + 69)], [None for _ in range(n + 69)]
        for i in range(n):
            if (int(s[i])): nx1[i] = i
            else: nx0[i] = i
        for i in range(n - 2, -1, -1):
            if (nx0[i + 1] and nx0[i] == None): nx0[i] = nx0[i + 1]
        if(nx0[0] == n): print(0); return
        for i in range(n - 2, -1, -1):
            if (nx1[i + 1] and nx1[i] == None): nx1[i] = nx1[i + 1]
        posi = nx1[0] + 1
        for i in range(n):
            if (nx0[i] == None): nx0[i] = n
            if (nx1[i] == None): nx1[i] = n
        for i in range(n - 1, -1, -1):
            dp0[i] = dp0[i + 1]
            if (nx1[i] < n):
                if (int(s[i])): pass
                elif (not(int(s[i]))):
                    check_val = dp0[nx1[i] + 1]
                    dp0[i] = max(dp0[i],  check_val + 1)
                else: assert (False)
            if (nx0[i] < n):
                if (not (int(s[i]))): pass
                elif (int(s[i])):
                    check_val = dp0[nx0[i] + 1]
                    dp0[i] = max(dp0[i], check_val + 1)
                else: assert (False)
        for i in range(n - 1, -1, -1):
            if (nx1[i] < n):
                check_val = dp0[nx1[i] + 1]
                dp1[i] = max(dp1[i], check_val + 1)
        print('1', end='')
        start_posi, end_posi = 1, dp0[0] + (2 if (dp0[0] != dp1[0]) else 1)
        while (1):
            posi_shift = -1
            if(start_posi >= end_posi): print(); return
            if((~(posi - n)) < 0): print(0, end='')
            elif((~(nx0[posi] - n)) < 0): print(0, end=''); posi_shift = 0
            elif((~(dp0[nx0[posi] + 1] - dp1[0] + start_posi)) >= 0): print(0, end=''); posi_shift = 0
            else: print(1, end=''); posi_shift = 1
            if(posi_shift != -1): posi = 1 + (nx1[posi] if (posi_shift) else nx0[posi])
            start_posi += 1


def main():
    # orig_stdin = sys.stdin
    # orig_stdout = sys.stdout
    # f1 = open("D:\\n1\\New folder\\cp\\in.txt", 'r')
    # f2 = open("D:\\n1\\New folder\\cp\\out.txt", 'w')
    # sys.stdin = f1
    # sys.stdout = f2
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()
    # sys.stdin = orig_stdin
    # sys.stdout = orig_stdout
    # f1.close()
    # f2.close()


if __name__ == "__main__":
    main()
