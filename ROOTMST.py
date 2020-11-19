'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
from itertools import combinations
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


# class Gao:
#     def __init__(self, vrtcs): self.V = vrtcs; self.graph = []
#     def aE(self, u, v, w): self.graph.append([u, v, w])
#     def dhundh(self, prnt, i):
#         if prnt[i] == i: return i
#         return self.dhundh(prnt, prnt[i])
#     def un(self, prnt, rnk, x, y):
#         xr, yr = self.dhundh(prnt, x), self.dhundh(prnt, y)
#         if(rnk[xr] < rnk[yr]): prnt[xr] = yr
#         elif(rnk[xr] > rnk[yr]): prnt[yr] = xr
#         else: prnt[yr] = xr; rnk[xr] += 1
#     def jaadu(self):
#         res, _, e = [], 0, 0
#         self.graph = sorted(self.graph, key=lambda _: _[2])
#         prnt, rnk = [], []
#         for nd in range(self.V): prnt.append(nd); rnk.append(0)
#         while(e < self.V - 1):
#             u, v, w = self.graph[_]
#             _ += 1
#             x, y = self.dhundh(prnt, u), self.dhundh(prnt, v)
#             if(x != y): e += 1; res.append([u, v, w]); self.un(prnt, rnk, x, y)
#         finans = 0
#         for _ in res:
#             print(_[0], _[1])
#             finans += (_[2])
#         print(finans)
#         print()
#         return (finans)

N = 10000


def pehla_kaam(x, gr1, vis1):
    vis1[x] = True
    if x not in gr1:
        gr1[x] = {}
    for i in gr1[x]:
        if (not vis1[i]): pehla_kaam(i, gr1, vis1)


def dusra_kaam(x, gr2, vis2):
    vis2[x] = True
    if x not in gr2:
        gr2[x] = {}
    for i in gr2[x]:
        if (not vis2[i]): dusra_kaam(i, gr2, vis2)


def jaadu(n, gr1, gr2):
    vis1 = [False] * N
    pehla_kaam(1, gr1, vis1)
    vis2 = [False] * N
    dusra_kaam(1, gr2, vis2)
    for i in range(1, n + 1):
        if (not vis1[i] and not vis2[i]): return False
    return True


def main():
    n, tot = readints()
    if(n > 5): raise('Chalo bhai, mai chalta hu')
    if(tot > (n * (n - 1) // 2)): raise('Chutiya samjha hai?!')
    edges = [readarri() for _ in range(tot)]
    overall = [list(combinations(edges, i)) for i in range(1, n)]
    # for i in overall:
    #     print(i)
    ans = []
    # ANS = []
    for k in range(1, n):
        minans = 6969696969
        # ANS.append([])
        for msts in overall:
            for _ in msts:
                gr1, gr2 = {}, {}
                temp, corners, sum1 = [], set(), 0
                for j in _:
                    temp.append(j[0]); corners.add(j[0])
                    temp.append(j[1]); corners.add(j[1])
                    sum1 += j[2]
                    u, v = j[0], j[1]
                    if u not in gr1: gr1[u] = []
                    if v not in gr2: gr2[v] = []
                    gr1[u].append(v)
                    gr2[v].append(u)
                    if v not in gr1: gr1[v] = []
                    if u not in gr2: gr2[u] = []
                    gr1[v].append(u)
                    gr2[u].append(v)
                # check whether index as k and spanning tree exists or not
                if((temp.count(1) == k) and (len(corners) == n) and jaadu(len(corners), gr1, gr2)):
                    # if(k == 2): print(_)
                    # ANS[-1].append(sum1)
                    if(minans > sum1):
                        minans = sum1
                        # if(k == 2): print(_)
        ans.append(minans)
    # print(ANS)
    print(*ans)


if __name__ == "__main__":
    main()

'''
4 5
1 2 4
1 4 5
1 3 8
3 4 6
2 3 7

17 15 17
'''