'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
import itertools
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


def bin_search(lst, val):
    n = len(lst)
    l = 0
    r = n - 1
    while(l <= r):
        mid = l + (n - r) // 2
        if(lst[mid] == val):
            return True
        if(lst[mid] < val):
            l = mid + 1
        else:
            r = mid - 1
    return False


def main():
    for _ in range(int(input())):
        n = int(input())
        knights = []
        for _ in range(n):
            x, y = map(int, input().split())
            knights.append([x, y])
        a, b = map(int, input().split())
        set_p = list()
        for i in knights:
            x, y = i[0], i[1]
            set_p.append([x + 1, y + 2])
            set_p.append([x + 2, y + 1])
            set_p.append([x + 2, y - 1])
            set_p.append([x + 1, y - 2])
            set_p.append([x - 2, y + 1])
            set_p.append([x - 1, y + 2])
            set_p.append([x - 1, y - 2])
            set_p.append([x - 2, y - 1])
            set_p.append([x + 1, y + 2])
            set_p.append([x + 2, y + 2])
        # print(set_p)
        finset = sorted(list(set_p for set_p ,_ in itertools.groupby(set_p)))
        cnt = 0
        if(bin_search(finset, [a - 1, b + 1])):
            cnt += 1
        if(bin_search(finset, [a, b + 1])):
            cnt += 1
        if(bin_search(finset, [a + 1, b + 1])):
            cnt += 1
        if(bin_search(finset, [a + 1, b])):
            cnt += 1
        if(bin_search(finset, [a + 1, b - 1])):
            cnt += 1
        if(bin_search(finset, [a, b - 1])):
            cnt += 1
        if(bin_search(finset, [a - 1, b - 1])):
            cnt += 1
        if(bin_search(finset, [a - 1, b])):
            cnt += 1
        print("YES" if cnt == 8 else "NO")


if __name__ == "__main__":
    main()
