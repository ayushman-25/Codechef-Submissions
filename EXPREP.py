'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
# import time
from io import BytesIO, IOBase
from collections import Counter

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


mod = 998244353

def modI(a, m):
    # GFG reference
    m0 = m
    y, x = 0, 1
    if (m == 1): return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x += m0
    return x


def main():
    # start_time = time.time()
    for _ in range(int(input())):
        s, w = input(), [int(i) for i in input().split()]
        sS = []
        n = len(s)
        p, q = 0, n * (n + 1) // 2
        wT = Counter()
        sZ = Counter()
        oA = ord('a')
        for i in range(n):
            tempS = ''
            tP = 0
            size = 0
            temp = []
            for j in range(i, n):
                tempS += s[j]
                tP += w[ord(s[j]) - oA]
                size += 1
                sZ[tempS] = size
                wT[tempS] = (tP % mod)
                temp.append(tempS)
            sS.append(temp)
            temp = []
        # tB = []
        start = n
        # print(sS)
        for i in sS:
            for j in range(start):
                # print(i[j])
                for k in range(0, j + 1):
                    # print(i[k], end=' ')
                    # i[j] check, iterating i[k];
                    if (j == k):
                        # print(1, i[k], i[j])
                        # tB.append(i[k])
                        p += wT[i[k]]
                    else:
                        if ((i[k] * (sZ[i[j]] // sZ[i[k]])) + (i[k][0: sZ[i[j]] % sZ[i[k]]]) == i[j]):
                            # print(2, i[k], i[j])
                            # tB.append(i[k])
                            p += wT[i[k]]
                # print()
            start -= 1
        print(((p % mod) * (modI(q, mod) % mod)) % mod)

if __name__ == "__main__":
    main()

'''
FOR 10 POINTS!!
'''