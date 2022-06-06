'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
import time
# from dataclasses import dataclass, field
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


# GFG REFERENCE for the implementation part of Kruskals MST
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/?ref=rp

class Gph:
    def __init__(self, vrtcs): self.V = vrtcs; self.graph = []
    def aE(self, u, v, w): self.graph.append([u, v, w])
    def dhundh(self, prnt, i):
        if prnt[i] == i: return i
        return self.dhundh(prnt, prnt[i])
    def un(self, prnt, rnk, x, y):
        xr = self.dhundh(prnt, x)
        yr = self.dhundh(prnt, y)
        if(rnk[xr] < rnk[yr]): prnt[xr] = yr
        elif(rnk[xr] > rnk[yr]): prnt[yr] = xr
        else: prnt[yr] = xr; rnk[xr] += 1
    def kMST(self):
        res, _, e = [], 0, 0
        # self.graph = sorted(self.graph, key=lambda _: _[2],reverse=True)
        prnt, rnk = [], []
        for nd in range(self.V): prnt.append(nd); rnk.append(0)
        while(e < self.V - 1):
            u, v, w = self.graph[_]
            _ += 1
            x, y = self.dhundh(prnt, u), self.dhundh(prnt, v)
            if(x != y): e += 1; res.append([u, v, w]); self.un(prnt, rnk, x, y)
        finans = 0
        mini = 9999999999
        maxi = 0
        req = 0
        for _ in res:
            print(_[0] + 1, '-', _[1] + 1, ':', _[2])
            finans += abs(_[2])
            req += 1
            # if(abs(_[2]) < mini): mini = abs(_[2])
            # if(abs(_[2]) > maxi): maxi = abs(_[2])
        sys.stdout.write('Ans: ' + str(finans) + "\n")
        # print(mini, maxi)
        # print(res)
        print('req', req)



def main():
    # st = time.time()
    n, dim = map(int, input().split())
    gg = Gph(n)
    points = [list(map(int, input().split())) for i in range(n)]
    # weights = []
    # t1 = time.time()
    temppp = []
    for i in range(n):
        temp = 1
        for j in range(i + 1, n):
            curr_w = 0
            for z in range(dim):
                curr_w += abs(points[i][z] - points[j][z])
            if(j == 12 or i == 12):
                print(i + 1, j + 1, curr_w)
            temppp.append([curr_w, i, i + temp])
            # gg.aE(i, i + temp, curr_w)
            temp += 1
    print('highest', n * (n - 1) // 2)
    temppp.sort(reverse=True)
    contset = set()
    cnt = 0
    for i in temppp:
        # if(i[1] in contset and i[2] in contset):
        #     continue
        # if((i[1] not in contset) or (i[2] not in contset)):
        gg.aE(i[1], i[2], i[0])
        print(i[1] + 1, '-', i[2] + 1, ':', i[0])
        cnt += 1
        contset.add(i[1])
        contset.add(i[2])
        if(len(contset) == n):
            break
    # print(min(tl), max(tl))
    print("cnt", cnt)
    gg.kMST()



if __name__ == "__main__":
    main()
