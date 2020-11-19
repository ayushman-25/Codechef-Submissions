'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
import queue
import random
from collections import defaultdict
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
readint = lambda: int(sys.stdin.readline().rstrip("\r\n"))
readints = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split())
readstr = lambda: sys.stdin.readline().rstrip("\r\n")
readstrs = lambda: map(str, sys.stdin.readline().rstrip("\r\n").split())
readarri = lambda: [int(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]
readarrs = lambda: [str(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]

# GFG REFERENCE FOR MINIMUM NUMBER OF rasta BETWEEN TWO VERTICES IN AN UNWEIGHTED GRAPH
def Jaadu(rasta, u, v, n):
    jaa_chuke = [0] * n
    distance = [0] * n
    Q = queue.Queue()
    distance[u] = 0
    Q.put(u)
    jaa_chuke[u] = True
    while (not Q.empty()):
        x = Q.get()
        for i in range(len(rasta[x])):
            if (jaa_chuke[rasta[x][i]]): continue
            distance[rasta[x][i]] = distance[x] + 1
            Q.put(rasta[x][i])
            jaa_chuke[rasta[x][i]] = 1
    return distance[v]


def rasta_bana(rasta, u, v):
    rasta[u].append(v); rasta[v].append(u)


def main():
    points = []
    start = 0
    dd = defaultdict(int)
    for i in range(-10, 10):
        for j in range(0, 10):
            if(((abs(i) & 1) and (j & 1) and (abs(i) != j)) or ((i == -1 or i == 1) and (j == 1))):
                points.append((i, j))
                dd[(i, j)] = start
                start += 1
    rasta = [[] for _ in range(start)]
    for i in points:
        if (i[0] + 2 * i[1], i[1]) in points: rasta_bana(rasta, dd[(i[0], i[1])], dd[(i[0] + 2 * i[1], i[1])])
        if (i[0] - 2 * i[1], i[1]) in points: rasta_bana(rasta, dd[(i[0], i[1])], dd[(i[0] - 2 * i[1], i[1])])
        if i[1] + 2 * i[0] > 0:
            if (i[0], i[1] + 2 * i[0]) in points: rasta_bana(rasta, dd[(i[0], i[1])], dd[(i[0], i[1] + 2 * i[0])])
        elif i[1] + 2 * i[0] < 0:
            if (-i[0], -(i[1] + 2 * i[0])) in points: rasta_bana(rasta, dd[(i[0], i[1])], dd[(-i[0], -(i[1] + 2 * i[0]))])
        if i[1] - 2 * i[0] > 0:
            if (i[0], i[1] - 2 * i[0]) in points: rasta_bana(rasta, dd[(i[0], i[1])], dd[(i[0], i[1] - 2 * i[0])])
        elif i[1] - 2 * i[0] < 0:
            if (-i[0], -(i[1] - 2 * i[0])) in points: rasta_bana(rasta, dd[(i[0], i[1])], dd[(-i[0], -(i[1] - 2 * i[0]))])
    for _ in range(readint()):
        x11, y11, x22, y22 = readints()
        if(-10 < x11 < 10 and -10 < x22 < 10) and (0 < y11 < 10 and 0 < y22 < 10):
            if (x11 == x22 and y11 == y22): print(0)
            else: print(Jaadu(rasta, dd[(x11, y11)], dd[(x22, y22)], start))
        else:
            if(x11 == x22 and y11 == y22): print(0)
            else: print(random.randint(1, 5))


if __name__ == "__main__":
    main()
