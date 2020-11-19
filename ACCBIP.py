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


def f(n):
    return (n * (n - 1) * (n - 2) // 6)

def main():
    for _ in range(int(input())):
        n, c, k = map(int, input().split())
        p_d = [0] * c
        for _ in range(n):
            a, b, c = map(int, input().split())
            p_d[c - 1] += 1
        V = [int(i) for i in input().split()]
        if (len(set(V)) == 1):
            p_d.sort(reverse=True)
            # print(p_d)
            # i = 0
            while (1):
                # print(k, p_d)
                if (k < V[0]):
                    break
                minsum = int(1e13) + 69
                minidx = -69
                for j in range(c):
                    sum1 = 0
                    for z in range(c):
                        if(p_d[z] >= 3):
                            if(z == j):
                                sum1 += f(p_d[z] - 1)
                            else:
                                sum1 += f(p_d[z])
                        # print("sum: ", sum1)
                    if(sum1 < minsum):
                        minsum = sum1
                        minidx = j
                p_d[minidx] -= 1
                k -= V[0]
                # print(k)
            ans = 0
            for i in p_d:
                if(i >= 3):
                    ans += f(i)
            print(ans)

if __name__ == "__main__":
    main()
