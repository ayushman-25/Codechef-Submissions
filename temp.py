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
# from heapq import *
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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
readint = lambda: int(sys.stdin.readline().rstrip("\r\n"))
readints = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split())
readstr = lambda: sys.stdin.readline().rstrip("\r\n")
readstrs = lambda: map(str, sys.stdin.readline().rstrip("\r\n").split())
readarri = lambda: [int(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]
readarrs = lambda: [str(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]

mod = 998244353
MOD = int(1e9) + 7
printt = []


def DFSUtil(v, visited, adj):
    visited.add(v)
    printt.append(v)
    for neighbour in adj[v]:
        if neighbour not in visited:
            DFSUtil(neighbour, visited, adj)


def DFS(v, adj):
    visited = set()
    DFSUtil(v, visited, adj)


def solve():
    global printt
    n = readint()
    arr = readarri()
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        adj[arr[i] - 1].append(i + 1)
    for _ in range(readint()):
        node, tasks = readints()
        DFS(node - 1, adj)
        for i in range(len(printt)): printt[i] += 1
        assigned_tasks = defaultdict(int)
        assigned_tasks[printt[0]] = tasks
        tl = []
        for i in range(1, len(printt)):
            # print('child', printt[i], 'baap', arr[printt[i] - 2])
            curr = printt[i]
            baap = arr[curr - 2]
            baap_ke_task = assigned_tasks[baap]
            if(baap_ke_task == -1): continue
            baap_ke_bache = len(adj[baap - 1])
            # print(baap_ke_task, baap_ke_bache)
            if(baap_ke_task / baap_ke_bache != baap_ke_task // baap_ke_bache):
                # print(curr, 'not assigned')
                print(baap_ke_task, baap_ke_bache)
                # ans += (baap_ke_task // baap_ke_bache)
                tl.append(baap_ke_task)
                assigned_tasks[curr] = -1
            else:
                # print(curr, 'assigned')
                # print(baap, baap_ke_bache, baap_ke_task)
                # print('add', baap_ke_task, baap_ke_bache)
                # ans += baap_ke_task // baap_ke_bache
                # tasks -= baap_ke_task // baap_ke_bache
                assigned_tasks[curr] = baap_ke_task // baap_ke_bache
        fin = sum(list(set(tl)))
        print(tasks - fin)
        printt = []


def main():
    t = 1
    # t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
