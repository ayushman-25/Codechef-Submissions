'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

import os
import sys
from collections import defaultdict
from fractions import Fraction
# from itertools import *
from math import gcd
from queue import Queue
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


def add(val1, val2):
    return (val1 % MOD + val2 % MOD) % MOD


def mult(val1, val2):
    return (val1 % MOD * val2 % MOD) % MOD


# References - https://www.geeksforgeeks.org/fraction/
def addFraction(n1, d1, n2, d2):
    d3 = gcd(d1, d2)
    d3 = (d1 * d2) // d3
    n3 = (((n1 * d3) // d1) + ((n2 * d3) // d2))
    common_factor = gcd(n3, d3)
    d3 = (d3 // common_factor)
    n3 = (n3 // common_factor)
    if(n3 < 0 and d3 < 0):
        return [abs(n3), abs(d3)]
    if(d3 < 0):
        return [-n3, abs(d3)]
    return [n3, d3]


def updateBIT(BITree, n, index, val):
    index += 1
    while(index <= n):
        temp = addFraction(BITree[index][0], BITree[index][1], val[0], val[1])
        BITree[index] = temp
        index += index & (-index)


def ConstructBITree(arr, n):
    BITree = [[0, 1] for _ in range(n + 1)]
    for i in range(n):
        updateBIT(BITree, n, i, arr[i])
    return BITree


def getSum(BITree, index):
    ans = [0, 1]
    index += 1
    while(index > 0):
        temp = addFraction(ans[0], ans[1], BITree[index][0], BITree[index][1])
        ans = temp
        index -= index & (-index)
    return ans


def update(BITree, l, r, n, val):
    updateBIT(BITree, n, l, [val[0], val[1]])
    updateBIT(BITree, n, r + 1, [-val[0], val[1]])


def solve():
    n, q = map(int, input().split())
    adj = [[] for _ in range(n)]
    for __ in range(n - 1):
        x, y = map(int, input().split())
        adj[x - 1].append(y - 1)
        adj[y - 1].append(x - 1)
    cnt1, cnt2 = 0, 0
    req_root = None
    for i in range(n):
        if (len(adj[i])) == 1:
            req_root = i
            cnt1 += 1
        if (len(adj[i])) == 2:
            cnt2 += 1
    if (cnt1 == 2 and cnt2 == n - 2):
        flattened_array = []
        visited = [0 for _ in range(n)]
        queue = [req_root]
        while(queue):
            parent = queue.pop(0)
            visited[parent] = 1
            flattened_array.append(parent)
            for i in adj[parent]:
                if(not(visited[i])):
                    queue.append(i)
        store_index = defaultdict(int)
        for i in range(n):
            store_index[flattened_array[i]] = i
        arr = [[0, 1] for _ in range(n)]
        BITree = ConstructBITree(arr, n)
        last = 0
        for _ in range(q):
            query = readarri()
            if(query[0] == 1):
                city = (last + query[1]) % n + 1
                city -= 1
                distance = (last + query[2]) % n + 1
                position = store_index[city]
                update(BITree, store_index[city], store_index[city], n, [1, 1])
                if(position == 0):
                    update(BITree, 1, distance if (distance < n) else n - 1, n, [1, 1])
                elif(position == n - 1):
                    update(BITree, n - 1 - distance - 1 if (distance < n) else 0, n - 2, n, [1, 1])
                else:
                    update(BITree, position + 1, position + distance if(position + distance < n) else n - 1, n, [1, 2])
                    update(BITree, position - distance if(position - distance >= 0) else 0, position - 1, n, [1, 2])
            else:
                u = (last + query[1]) % n + 1
                u -= 1
                fraction = getSum(BITree, store_index[u])
                last = (mult(fraction[0], pow(fraction[1], MOD - 2, MOD)))
                print(last)
    else:
        last = 0
        originals = [[] for _ in range(n)]
        for _ in range(q):
            check = readarri()
            probs = [0 for _ in range(n)]
            if (check[0] == 1):
                u = (last + check[1]) % n + 1
                d = (last + check[2]) % n + 1
                u -= 1
                probs[u] = 1
                root = u
                sons = [0 for _ in range(n)]
                visited = [0 for _ in range(n)]
                queue = [root]
                while (queue):
                    parent = queue.pop(0)
                    visited[parent] = 1
                    for i in adj[parent]:
                        if (not (visited[i])):
                            queue.append(i)
                            sons[parent] += 1
                visited = [0 for _ in range(n)]
                queue = [root]
                depth = [0 for _ in range(n)]
                while (queue):
                    parent = queue.pop(0)
                    visited[parent] = 1
                    for i in adj[parent]:
                        if (not (visited[i])):
                            queue.append(i)
                            depth[i] = depth[parent] + 1
                            if (depth[i] <= d):
                                probs[i] = sons[parent] * probs[parent]
                for i in range(n):
                    originals[i].append(probs[i])
            else:
                u = (last + check[1]) % n + 1
                u -= 1
                if (not (sum(originals[u]))):
                    print(0)
                    last = 0
                else:
                    if (len(originals[u]) == 1):
                        ans = mult(1, pow(originals[u][0], MOD - 2, MOD))
                        print(ans)
                        last = ans
                    else:
                        n1 = 1 if (originals[u][0]) else 0
                        d1 = originals[u][0] if (originals[u][0]) else 1
                        for i in range(1, len(originals[u])):
                            n2 = 1
                            d2 = originals[u][i]
                            if (d2):
                                res = addFraction(n1, d1, n2, d2)
                                n1 = res[0]
                                d1 = res[1]
                        ans = mult(n1, pow(d1, MOD - 2, MOD))
                        print(ans)
                        last = ans


def main():
    # orig_stdin = sys.stdin
    # orig_stdout = sys.stdout
    # f1 = open("D:\\n1\\New folder\\cp\\in.txt", 'r')
    # f2 = open("D:\\n1\\New folder\\cp\\out.txt", 'w')
    # sys.stdin = f1
    # sys.stdout = f2
    t = 1
    # t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()
    # sys.stdin = orig_stdin
    # sys.stdout = orig_stdout
    # f1.close()
    # f2.close()


if __name__ == "__main__":
    main()
