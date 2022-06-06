'''

* Author : Ayushman Chahar #
* About  : IT Sophomore    #
* Insti  : VIT, Vellore    #

'''

# import os
import sys
# from collections import *
# from itertools import *
# from math import *
# from queue import *
# from heapq import *
# from bisect import *
# from io import BytesIO, IOBase

# BUFSIZE = 8192


# class FastIO(IOBase):
#     newlines = 0
# 
#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None
# 
#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()
# 
#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()
# 
#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)
# 
# 
# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")
# 
# 
# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")
# readint = lambda: int(sys.stdin.readline().rstrip("\r\n"))
# readints = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split())
# readstr = lambda: sys.stdin.readline().rstrip("\r\n")
# readstrs = lambda: map(str, sys.stdin.readline().rstrip("\r\n").split())
# readarri = lambda: [int(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]
# readarrs = lambda: [str(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]


def check(curr, n, k):
    curr = curr.copy()
    dp = [[0 for _ in range(2 * k + 1)] for _ in range(n)]
    if(n == 1): return 0
    for _ in range(n): dp[_][0] = 1
    bc = 0
    for i in range(1, n):
        for z in range(1, 2 * k + 1):
            if(z >= curr[i]): dp[i][z] = (dp[i - 1][z] or dp[i - 1][z - curr[i]])
            else: dp[i][z] = dp[i - 1][z]
            if(i + 1 == n and z >= k and dp[i][z]):
                bc = 1; break
        if(bc): break
    sbst = []
    # sys.stdout.write(i, z)
    row = i; column = z
    while(1):
        if(not(column) or not(row)): break
        if(dp[row][column] and not(dp[row - 1][column]) and dp[row - 1][column - curr[row]]):
            sbst.append(curr[row])
            column -= curr[row]
        row -= 1
    # sys.stdout.write("first", sbst)
    # sys.stdout.write("S", sum(sbst))
    if(sum(sbst) >= k):
        for i in sbst:
            curr.remove(i)
        # print(*sbst)
        sbssst = sbst.copy()
        # sys.stdout.write("left1", curr)
        sc = sum(curr)
        if(sc < k):
            return 0
        elif(sc == k):
            return n
        last = len(sbst)
        n = len(curr)
        if (sc >= k and n == 1):
            return last + 1
        dp = [[0 for _ in range(2 * k + 1)] for _ in range(n)]
        for _ in range(n): dp[_][0] = 1
        bc = 0
        for i in range(1, n):
            for z in range(1, 2 * k + 1):
                if (z >= curr[i]):
                    dp[i][z] = (dp[i - 1][z] or dp[i - 1][z - curr[i]])
                else:
                    dp[i][z] = dp[i - 1][z]
                if (i + 1 == n and z >= k and dp[i][z]):
                    # sys.stdout.write("break", z)
                    bc = 1; break
            if (bc): break
        sbst = []
        row = i; column = z
        # for ii in range(i + 1):
        #     for zz in range(z + 1):
        #         sys.stdout.write(dp[ii][zz], end=" ")
        #     sys.stdout.write()
        # sys.stdout.write(i, z)
        while (1):
            # sys.stdout.write(row, column)
            if(not(row) or not(column)): break
            if (dp[row][column] and not(dp[row - 1][column]) and (dp[row - 1][column - curr[row]])):
                sbst.append(curr[row])
                column -= curr[row]
            row -= 1
        # sys.stdout.write("second", sbst)
        if(sum(sbst) >= k):
            print(*sbssst)
            print(*sbst)
            return last + len(sbst)
        else: return 0
    else:
        # sys.stdout.write("hereeee")
        return 0


def solve():
    n, k = map(int, sys.stdin.readline().split())
    arr = sorted([int(i) for i in sys.stdin.readline().split()], reverse=True)
    # sys.stdout.write(max(arr))
    if(n == 1):
        sys.stdout.write("-1\n")
        return
    if(max(arr) >= k):
        ans = 1
        sum1 = 0
        for i in range(1, n):
            if(sum1 >= k):
                sys.stdout.write(str(ans) + "\n")
                return
            sum1 += arr[i]
            ans += 1
        if(sum1 < k):
            sys.stdout.write("-1\n")
            return
    curr = []
    sum1 = 0
    for i in range(n):
        if(sum1 >= 2 * k):
            break
        sum1 += arr[i]
        curr.append(arr[i])
    if(sum1 < 2 * k):
        sys.stdout.write("-1\n")
        return
    curr = curr[::-1]
    lc = len(curr)
    while(1):
        val = check(curr, lc, k)
        if(not(val)):
            if(i == n):
                break
            curr = [arr[i]] + curr
            # curr.insert(0, arr[i])
            i += 1
            lc += 1
        else:
            sys.stdout.write(str(val) + "\n")
            return
    sys.stdout.write("-1\n")


def main():
    t = 1
    t = int(sys.stdin.readline())
    for _ in range(t):
        # print("Case #" + str(_) +": ")
        solve()


if __name__ == "__main__":
    main()
