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


def main():
    for _ in range(int(input())):
        n, x, p, k = map(int, input().split())
        # make x as pth smallest using kth smallest
        p -= 1
        k -= 1
        arr = sorted([int(i) for i in input().split()])
        ans = 0
        if(x not in arr):
            arr[k] = x
            arr.sort()
            ans += 1
        if(arr.count(x) == 1):
            curr = arr.index(x)
            if (arr[p] == x):
                print(ans)
                continue
            if (arr[p] < x):
                if(p >= k):
                    ans += abs(curr - p)
                    print(ans)
                else:
                    print(-1)
                continue
            if (arr[p] > x):
                if(k >=  p):
                    ans += abs(curr - p)
                    print(ans)
                else:
                    print(-1)
        else:
            indexes = [arr.index(x), n - 1 - arr[::-1].index(x)]
            # for i in range(n):
            #     if(arr[i] == x):
            #         indexes.append(i)
            # print(indexes)
            anss = []
            for i in indexes:
                ans = 0
                curr = i
                if (arr[p] == x):
                    anss.append(ans)
                if (arr[p] < x):
                    if (p >= k):
                        ans += abs(curr - p)
                        anss.append(ans)
                    else:
                        anss.append(-1)
                if (arr[p] > x):
                    if (k >= p):
                        ans += abs(curr - p)
                        anss.append(ans)
                    else:
                        anss.append(-1)
            if all(i == -1 for i in anss):
                print(-1)
            else: print(min(anss))


if __name__ == "__main__":
    main()

