'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
# from collections import defaultdict
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


def main():
    n, q = map(int, input().split())
    h = [int(i) for i in input().split()]
    s = [int(i) for i in input().split()]
    # dl = defaultdict(int)
    # for i in range(len(s)):
    #     dl[i + 1] += s[i]
    for _ in range(q):
        a, b, c = map(int, input().split())
        if (a == 1):
            s[b - 1] = c
        else:
            # journey from point b to point c
            if(n == 1):
                print(s[b - 1])
                continue
            if (abs(b - c) == 1):
                if (h[b - 1] <= h[c - 1]):
                    print(-1)
                    continue
                else:
                    print(s[b - 1] + s[c - 1])
                    continue
            if (b == c):
                print(s[b - 1])
                continue
            # if (b == 1):
            #     if (h[b] >= h[b - 1]):
            #         print(-1)
            #         continue
            # if (b == n):
            #     if (h[b - 2] >= h[b - 1]):
            #         print(-1)
            #         continue
            # if (b > 1 and b < n):
            #     if (h[b] <= h[b - 1]) and (h[b] <= h[b + 1]):
            #         print(-1)
            #         continue
            if (b < c):
                ch = h[b - 1: c][::-1]
                sp = s[b - 1: c][::-1]
                tot_spices = s[c - 1]
                pts = [i for i in range(b, c + 1)][::-1]
            else:
                ch = h[c - 1: b]
                sp = s[c - 1: b]
                tot_spices = s[c - 1]
                pts = [i for i in range(c, b + 1)]
            ans = True
            for i in range(1, len(ch) - 1):
                if (ch[i] >= h[b - 1]) and (ch[i] >= h[c - 1]):
                    print(-1)
                    ans = False
                    break
            if (ans):
                # print(ch)
                # print(sp)
                start = ch[0]
                found = False
                reached_end = False
                for i in range(1, len(ch)):
                    if ch[i] > start:
                        # print("val", ch[i])
                        # print("1", tot_spices)
                        tot_spices += s[pts[i] - 1]
                        # print("2", tot_spices)
                        start = ch[i]
                        found = True
                    if(i == len(ch) - 1):
                        reached_end = True
                if not reached_end:
                    print(-1)
                    continue
                if not found:
                    print(-1)
                    continue
                print(tot_spices)

if __name__ == "__main__":
    main()

