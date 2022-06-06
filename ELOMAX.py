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
readarr = lambda: [int(i) for i in input().split()]

def main():
    for _ in range(int(input())):
        n, m = (map(int, input().split()))
        ratings = readarr()
        peak_ratings = [0] * n
        peak_rankings = [n + 1] * n
        rankings = []
        answers = ["N"] * n
        rating_changes = [readarr() for _ in range(n)]
        for p in range(m):
            new_rankings = []
            if not rankings:
                for i in range(n):
                    ratings[i] += rating_changes[i][p]
                    new_rankings.append((i, ratings[i]))
            else:
                for i, j in rankings:
                    ratings[i] += rating_changes[i][p]
                    new_rankings.append((i, ratings[i]))
            new_rankings.sort(reverse=True, key=lambda x: x[1])
            prev_rating = None
            rank = 0
            for i in range(n):
                x, y = new_rankings[i]
                if prev_rating != y:
                    rank = i
                if ratings[x] > peak_ratings[x] and rank < peak_rankings[x]:
                    peak_ratings[x] = ratings[x]
                    peak_rankings[x] = rank
                    answers[x] = "Y"
                elif ratings[x] > peak_ratings[x]:
                    peak_ratings[x] = ratings[x]
                    answers[x] = "N"
                elif rank < peak_rankings[x]:
                    peak_rankings[x] = rank
                    answers[x] = "N"
                prev_rating = y
            rankings = new_rankings
        print(answers.count("N"))

if __name__ == "__main__":
    main()
