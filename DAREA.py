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


def do(n, dd, arr, ma, mi):
    myarr = sorted(list(dd.keys()))
    myarr_check = defaultdict(int)
    for i in myarr: myarr_check[i] = 1
    start, end = 0, len(dd.keys()) - 1
    a1, a2 = 0, int(1e19) + 69
    Areas_pos = []
    for _ in range(n - 1):
        if(dd[arr[_][1]]):
            dd[arr[_][1]] -= 1
            if(not dd[arr[_][1]]):
                dd.pop(arr[_][1])
                if(dd[ma] == 0):
                    end -= 1
                    ma = myarr[end]
                elif(dd[mi] == 0):
                    start += 1
                    mi = myarr[start]
                else:
                    myarr.remove(arr[_][1])
                    end -= 1
        Areas_pos.append((-arr[_ + 1][0] + arr[n - 1][0]) * (ma - mi) + (-arr[0][0] + arr[_][0]) * (max(a1, arr[_][1]) - min(a2, arr[_][1])))
        a1 = max(arr[_][1], a1); a2 = min(arr[_][1], a2)
    if not Areas_pos:
        Areas_pos.extend([0])
    return min(Areas_pos)


def solve():
    n = readint()
    x_p, y_p = list(), list()
    for _ in range(n):
        a, b = readints()
        y_p.append([b, a])
        x_p.append([a, b])
    x_d, y_d = defaultdict(int), defaultdict(int)
    for [a, b] in y_p:
        y_d[a] += 1
        x_d[b] += 1
    print(min(do(n, y_d, sorted(x_p), max(list(y_d.keys())), min(list(y_d.keys()))), do(n, x_d, sorted(y_p), max(list(x_d.keys())), min(list(x_d.keys())))))


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
