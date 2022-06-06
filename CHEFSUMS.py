'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
from math import factorial
from itertools import combinations
from itertools import groupby
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

MOD = int(1e9) + 7


# gfg ref
def find_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def main():
    N, k, m, x = map(int, input().split())
    arr = [int(i) for i in input().split()]
    A = [i for i in set(combinations(arr * k, k))]
    A = [sorted(i) for i in A]
    A.sort()
    # print(A)
    tA = list(A for A, _ in groupby(A))
    # print(tA)
    kFac = factorial(k)
    summ = 0
    for i in tA:
        i = [j for j in i]
        gcd = i[0]
        s, p = 0, 1
        for j in range(1, k):
            gcd = find_gcd(gcd, i[j])
        for j in i:
            s += (pow(j, x, MOD))
        for j in i:
            p = (p % MOD * j % MOD) % MOD
        P = pow(p, m, MOD)
        sD = -1
        if (p % 2 == 0):
            sD = 2
        else:
            j = 3
            while (j * j <= p):
                if (p % j == 0):
                    sD = j
                    break
                j += 2
            if (sD == -1): sD = j
        # print(gcd, s, P, sD)
        temp = (gcd % MOD * s % MOD * P % MOD * sD % MOD) % MOD
        if (i[0] != i[-1]):
            temp = (temp % MOD * kFac % MOD) % MOD
        summ = (summ % MOD + temp % MOD) % MOD
        # print(temp)
    print(summ)


if __name__ == "__main__":
    main()
