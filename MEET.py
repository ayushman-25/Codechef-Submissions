'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
from datetime import datetime, time
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
    p = readarrs()
    hrs = int(p[0][:2])
    mins = int(p[0][3:])
    if(hrs == 12 and p[-1] == 'AM'): hrs = 0
    hrs = hrs + 12 if(p[1] == 'PM' and hrs != 12) else hrs
    check_time = time(hrs, mins)
    ans = ''
    for _ in range(readint()):
        timee = readarrs()
        hrs_start, mins_start = int(timee[0: 2][0][:2]), int(timee[0: 2][0][3:])
        if(hrs_start == 12 and timee[1] == 'AM'): hrs_start = 0
        hrs_start = hrs_start + 12 if(timee[1] == 'PM' and hrs_start != 12) else hrs_start
        hrs_end, mins_end = int(timee[2:][0][:2]), int(timee[2:][0][3:])
        if (hrs_end == 12 and timee[3] == 'AM'): hrs_end= 0
        hrs_end = hrs_end + 12 if (timee[3] == 'PM' and hrs_end != 12) else hrs_end
        if(time(hrs_start, mins_start) < time(hrs_end, mins_end)):
            ans += '1' if (check_time >= time(hrs_start, mins_start) and check_time <= time(hrs_end, mins_end)) else '0'
        elif(time(hrs_start, mins_start) > time(hrs_end, mins_end)):
            ans += '1' if (check_time >= time(hrs_start, mins_start) or check_time <= time(hrs_end, mins_end)) else '0'
        else:
            ans += '1' if(check_time == time(hrs_start, mins_start) == time(hrs_end, mins_end)) else '0'
    print(ans)


def main():
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
