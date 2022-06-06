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


# ref GFG
mod = 998244353
SIZE = 26

def binomialCoeff(n, r):
    num = den = 1
    if (r > n - r):
        r = (n % mod - r % mod) % mod
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    return (num * pow(den, mod - 2, mod)) % mod

def countSubsequences(str1, str2):
    freq1 = [0 for i in range(26)]
    freq2 = [0 for i in range(26)]
    n1 = len(str1)
    n2 = len(str2)
    for i in range(0, n1):
        freq1[ord(str1[i]) - ord('a')] += 1
    for i in range(0, n2):
        freq2[ord(str2[i]) - ord('a')] += 1
    count = 1
    for i in range(0, SIZE):
        if (freq2[i] != 0):
            if (freq2[i] <= freq1[i]):
                count = ((count % mod) * (binomialCoeff(freq1[i], freq2[i]) % mod)) % mod
            else:
                return 0
    return count

def main():
    for _ in range(int(input())):
        str = input()
        n = int(input())
        ladies = [input() for _ in range(n)]
        values = [countSubsequences(str, i) % mod for i in ladies]
        for i in values: print(i)
        if(values.count(0) == n): print("No Research This Month")
        else: print(ladies[values.index(max(values))])

if __name__ == "__main__":
    main()
