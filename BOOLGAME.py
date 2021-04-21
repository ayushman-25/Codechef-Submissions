'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
from collections import defaultdict
# from itertools import *
# from math import *
# from queue import *
import heapq
# from bisect import *
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


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
readint = lambda: int(sys.stdin.readline().rstrip("\r\n"))
readints = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split())
readstr = lambda: sys.stdin.readline().rstrip("\r\n")
readstrs = lambda: map(str, sys.stdin.readline().rstrip("\r\n").split())
readri = lambda: [int(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]
readrs = lambda: [str(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]

sys.setrecursionlimit(int(1e6) + 69)


def tryall(single_1, ans, n, score, curr_ind, initi):
    if(curr_ind - 1 == n): return score[(initi, curr_ind - 1)] if (~(initi - curr_ind) >= 0 and initi) else 0
    if(ans[curr_ind][initi] + 1): return ans[curr_ind][initi]
    if(initi):
        ans[curr_ind][initi] = max(-(1 << 64), single_1[curr_ind] + tryall(single_1, ans, n, score, curr_ind + 1, initi), score[(initi, curr_ind - 1)] + tryall(single_1, ans, n, score, curr_ind + 1, 0))
        return ans[curr_ind][initi]
    check = tryall(single_1, ans, n, score, curr_ind + 1, curr_ind)
    ans[curr_ind][initi] = max(check + single_1[curr_ind], tryall(single_1, ans, n, score, curr_ind + 1, initi))
    return ans[curr_ind][initi]


def solve():
    n, m, k = readints()
    single_1 = readri()
    cons_1 = [readri() for _ in range(m)]
    if(n <= 18):
        a = list()
        for i in range(1 << n):
            score = 0
            checkbin = bin(i).replace("0b", '')
            checkbin = '0' * (n - len(checkbin)) + checkbin
            prefix = [int(checkbin[0])]
            for j in range(1, n): prefix.append(int(checkbin[j]) + prefix[-1])
            for j in range(n):
                if(checkbin[j] == '1'): score += single_1[j]
            for mm in cons_1:
                if(prefix[mm[1] - 1] - (0 if mm[0] == 1 else prefix[mm[0] - 2]) == mm[1] - mm[0] + 1): score += mm[2]
            a.append(score)
        print(*sorted(a, reverse=True)[0: k])
        return
    single_1 = [0] + single_1
    if(k == 1):
        curr_i, curr_p, ans, score = 0, 1, [[-1 for _ in range(69)] for _ in range(69)], defaultdict(int)
        # Consecutive range scores...
        for i in range(1, n + 1):
            for j in range(i, n + 1): score[(i, j)] = sum(cons_1[k][2] for k in range(m) if (cons_1[k][0] >= i and cons_1[k][1] <= j))
        print(tryall(single_1, ans, n, score, curr_p, curr_i))
        return
    ans, r, iter = [[[0, 0]]] + [[] for _ in range(n)], [[] for _ in range(n + 1)], 0
    for [a, b, c] in cons_1:
        r[a].append([iter, c]); r[b].append([iter, c])
        iter += 1
    for i in range(1, n + 1):
        temp = [[q1, q2] for [q1, q2] in ans[i - 1]]
        tpx = [[q1] for [q1, q2] in ans[i - 1]]
        tpy = [[q2] for [q1, q2] in ans[i - 1]]
        c, m, s, ln, sl, f, j = 0, 0, set(), len(temp), set(), 0, i
        while(69):
            if(j == 0): break
            m ^= (2 ** j); c += single_1[j]
            for [a, b] in r[j]:
                c += (0 if a not in s else b)
                if(a not in s): s.add(a)
            if(~j <= -3):
                for [a, b] in ans[j - 2]:
                    c2, c1 = m ^ b, a + c
                    tpx.append([c1]); tpy.append([c2])
                    ln += 1
            else: tpx.append([c]); tpy.append([m]); ln += 1
            j -= 1
        tpx.sort(reverse=True)
        tpy.sort(reverse=True)
        for j in range(ln):
            if(tpy[j][0] not in sl):
                ans[i].append([tpx[j][0], tpy[j][0]])
                f += 1
                if(f >= k): break
                sl.add(tpy[j][0])
    print(*[ans[n][i][0] for i in range(k)])


def main():
    # orig_stdin = sys.stdin
    # orig_stdout = sys.stdout
    # f1 = open("D:\\n1\\New folder\\cp\\in.txt", 'r')
    # f2 = open("D:\\n1\\New folder\\cp\\out.txt", 'w')
    # sys.stdin = f1
    # sys.stdout = f2
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()
    # sys.stdin = orig_stdin
    # sys.stdout = orig_stdout
    # f1.close()
    # f2.close()


if __name__ == "__main__":
    main()
