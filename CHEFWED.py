'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
from collections import Counter
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


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        F = [int(i) for i in input().split()]
        if(n == 1 and k == 2):
            print(2)
            continue
        if(n == 2 and k == 2):
            print(4)
            continue
        temP = [[]]
        for i in F:
            if i not in temP[-1]:
                temP[-1].append(i)
            else:
                temP.append([i])
        if(k == 1):
            print(len(temP))
            continue
        cT = Counter(F)
        # print(cT)
        ans1 = k
        # ans3 = 1
        for i in set(F):
            if(cT[i] > 1):
                ans1 += cT[i]
                # ans3 += cT[i]
        ans2 = len(temP) * k
        # print(temP)
        for i in temP:
            cTemp = Counter(i)
            for j in set(i):
                if(cTemp[j] > 1):
                    ans2 += cTemp[j]
        fA = min(ans1, ans2)
        # if(k == 2):
        #     if(n == 1):
        #         print(2)
        #         continue
        #     if(n == 2):
        #         print(4)
        #         continue
        #     tP = [[]]
        #     start = 0
        #
        #     stack = []
        #     for i in range(n):
        #         stack.append(F[i])
        #         if(len(stack) > 2):
        #             if(stack[-2] == stack[-3] and stack[-2] != stack[-1]):
        #                 for j in stack[:-1]:
        #                     tP[-1].append(j)
        #                 tP.append([stack[-1]])
        #                 stack = []
        #     # print(tP)
        #     ans = len(tP) * k
        #     for i in tP:
        #         cTe = Counter(i)
        #         for j in set(i):
        #             if(cTe[j] > 1):
        #                 ans += cTe[j]
        #     if(tP == [[]]):
        #         print(fA, tP)
        #     else:
        #         print(min(fA, ans), tP)
        #     continue
        # if(k == 2 and n >= 3):
        #     ans3 = 0
        #     sF = set(F)
        #     stack = []
        #     tpP = [[]]
        #     for i in F:
        #         stack.append(i)
        #         # print(stack)
        #         if(len(stack) == 3):
        #             if(stack[0] == stack[1] == stack[2]):
        #                 tpP[-1].append(stack[0])
        #                 tpP[-1].append(stack[1])
        #                 tpP[-1].append(stack[2])
        #                 stack = []
        #                 continue
        #             if(stack[0] == stack[2] != stack[1]):
        #                 tpP[-1].append(stack[0])
        #                 tpP[-1].append(stack[1])
        #                 tpP[-1].append(stack[2])
        #                 stack = []
        #                 continue
        #             if(stack[0] == stack[1] != stack[2]):
        #                 tpP[-1].append(stack[0])
        #                 tpP.append([stack[-2], stack[-1]])
        #                 stack = []
        #                 continue
        #             if(stack[0] != stack[1] == stack[2]):
        #                 tpP[-1].append(stack[0])
        #                 tpP[-1].append(stack[1])
        #                 tpP.append([stack[-1]])
        #                 stack = []
        #                 continue
        mini = int(1e9) + 1
        for i in range(n):
            arr1 = F[0: i + 1]
            arr2 = F[i + 1: n]
            a1, a2 = k, k
            c1 = Counter(arr1)
            c2 = Counter(arr2)
            for j in set(arr1):
                if (c1[j] > 1):
                    a1 += c1[j]
            for j in set(arr2):
                if (c2[j] > 1):
                    a2 += c2[j]
            mini = min(mini, a1 + a2)
        print(min(mini, fA))

if __name__ == "__main__":
    main()
