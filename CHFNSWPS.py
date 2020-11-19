'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
from io import BytesIO, IOBase
from collections import Counter
from collections import defaultdict

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
        A, B = list(map(int, input().split())), list(map(int, input().split()))
        if (n == 1):
            if (A[0] != B[0]):
                print(-1)
                continue
            else:
                print(0)
                continue
        if (sorted(A) == sorted(B)):
            print(0)
            continue
        combined_count = Counter(A + B).most_common(2 * n)
        ans = True
        for i in combined_count:
            if (i[1] & 1):
                ans = False
                print(-1)
                break
        if (ans):
            ACount = defaultdict(int)
            BCount = defaultdict(int)
            for i in A: ACount[i] += 1
            for i in B: BCount[i] += 1
            comb = set(A + B)
            minV = min(comb)
            minA, minB = [], []
            for i in comb:
                if ACount[i] != BCount[i]:
                    if ACount[i] > BCount[i]:
                        for j in range((ACount[i] - BCount[i]) // 2):
                            minA.append(i)
                    else:
                        for j in range((BCount[i] - ACount[i]) // 2):
                            minB.append(i)
                else:
                    pass
            SortedminA = sorted(minA)
            SortedminB = sorted(minB, reverse=True)
            print(SortedminA)
            print(SortedminB)
            ans = 0
            for i in range(len(minA)):
                if (2 * minV > min(SortedminA[i], SortedminB[i])):
                    ans += min(SortedminA[i], SortedminB[i])
                else:
                    ans += (2 * minV)
            print(ans)

if __name__ == "__main__":
    main()
