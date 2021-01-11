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


fh = 'abcdefgh'
sh = 'ijklmnop'


def solve():
    n = readint()
    s = readstr()
    for i in range(0, n, 4):
        gets = s[i: i + 4]
        if(gets[0] == '0'):
            if(gets[1] == '0'):
                if(gets[2] == '0'):
                    if(gets[3] == '0'): print(fh[0], end='')
                    else: print(fh[1], end='')
                else:
                    if(gets[3] == '0'): print(fh[2], end='')
                    else: print(fh[3], end='')
            else:
                if (gets[2] == '0'):
                    if (gets[3] == '0'): print(fh[4], end='')
                    else: print(fh[5], end='')
                else:
                    if (gets[3] == '0'): print(fh[6], end='')
                    else: print(fh[7], end='')
        else:
            if (gets[1] == '0'):
                if (gets[2] == '0'):
                    if (gets[3] == '0'): print(sh[0], end='')
                    else: print(sh[1], end='')
                else:
                    if (gets[3] == '0'): print(sh[2], end='')
                    else: print(sh[3], end='')
            else:
                if (gets[2] == '0'):
                    if (gets[3] == '0'): print(sh[4], end='')
                    else: print(sh[5], end='')
                else:
                    if (gets[3] == '0'): print(sh[6], end='')
                    else: print(sh[7], end='')
    print()


def main():
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_) +": ")
        solve()


if __name__ == "__main__":
    main()
