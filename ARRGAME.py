'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
from collections import Counter
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
    for _ in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        if (n == 1):
            print("No")
            continue
        if (n == 2):
            print("No")
            continue
        # max_so_fare = 0
        # max_so_faro = 0
        ans = []
        tc = 0
        for i in range(n):
            if (arr[i] == 0):
                tc += 1
            else:
                if (tc > 0):
                    ans.append(tc)
                tc = 0
        # print(ans)
        if (ans == []):
            print("No")
            continue
        if (len(ans) == 1):
            if (ans[0] & 1):
                print("Yes")
            else:
                print("No")
        else:
            ans.sort(reverse=True)
            t1, t2 = ans[0], ans[1]
            if (((t1 + 1) // 2) > t2 and (t1 & 1)):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
