'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
# from itertools import combinations
# from collections import deque
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

MOD = int(1e9) + 7

def main():
    for _ in range(int(input())):

        n = int(input())
        arr = sorted([int(i) for i in input().split()])

        if (n == 1):

            sys.stdout.write("2\n")
            continue

        maxCnt = arr.count(max(arr))

        if(maxCnt & 1):

            anS = pow(2, n, MOD)

            sys.stdout.write(str(anS) + "\n")
            continue

        #BRUTE FORCE!!!!
        # start = 1
        # buffer = tarr[0]
        # arr = []
        #
        # for i in range(n):
        #     if tarr[i] == buffer:
        #         arr.append(start)
        #     else:
        #         start += 1
        #         arr.append(start)
        #         buffer = tarr[i]
        #
        # # print(arr)
        #
        # combs = []
        #
        # for i in range(1, n + 1):
        #     combs.append(list(combinations(arr, i)))
        #
        # lists = [[]]
        #
        # for c in combs:
        #     for t in c:
        #         lists.append(list(t))
        #
        # # for i in lists:
        # #     print(i)
        #
        # start, count = 0, 0
        #
        # while (True):
        #     if(start == (2 ** n) // 2):
        #         break
        #
        #     l1 = deque(lists[start])
        #     l2 = deque(lists[2 ** n - start - 1])
        #
        #     l1L, l2L = len(l1), len(l2)
        #
        #     while(True):
        #         # print(l1, l2)
        #         if(l1L == 0 or l2L == 0):
        #             # print(l1, l2)
        #             count = (count % MOD + 1) % MOD
        #             break
        #
        #         else:
        #             s1, s2 = sorted(set(l1)), sorted(set(l2))
        #
        #             if(sorted(l1) == sorted(l2)):
        #                 # draw
        #                 break
        #
        #             if(s1 == s2):
        #                 # print(l1, l2)
        #                 count = (count % MOD + 1) % MOD
        #                 break
        #
        #             # if(s1 == s2 and sum(s1) == sum(s2)):
        #             #     # draw
        #             #     break
        #             #
        #             # if(len(s1) == len(s2) == 1 and l1[0]):
        #             #     count = (count % MOD + 1) % MOD
        #             #     break
        #
        #             # if(l1 == l2):
        #             #     # draw
        #             #     break
        #             #
        #             # if (len(set(l1)) == len(set(l2)) == 1 and l1[0] == l2[0]):
        #             #     # draw
        #             #     break
        #             #
        #             # if(l1L == l2L == 2):
        #             #     if(sorted(l2) == sorted(l1)):
        #             #         #draw
        #             #         break
        #
        #             if(l1[0] < l2[0]):
        #                 l2.append(l2[0])
        #                 l2.popleft()
        #                 l1[0] -= 1
        #                 if(l1[0] >= 0):
        #                     l2.append(l1[0])
        #                     l2L += 1
        #                 l1.popleft()
        #                 l1L -= 1
        #                 continue
        #
        #             if(l2[0] < l1[0]):
        #                 l1.append(l1[0])
        #                 l1.popleft()
        #                 l2[0] -= 1
        #                 if(l2[0] >= 0):
        #                     l1.append(l2[0])
        #                     l1L += 1
        #                 l2.popleft()
        #                 l2L -= 1
        #                 continue
        #
        #             if(l1[0] == l2[0]):
        #                 l1.append(l1[0])
        #                 l2.append(l2[0])
        #                 l1.popleft()
        #                 l2.popleft()
        #                 # l1L -= 1
        #                 # l2L -= 1
        #                 continue
        #
        #     start += 1
        #     # print(l1, l2)

        if(not(maxCnt & 1)):

            tempans = 1

            for _ in range(min((maxCnt >> 1), (maxCnt - (maxCnt >> 1)))):
                tempans = (tempans % MOD * (maxCnt - _) % MOD) % MOD
                tempans = (tempans % MOD * pow(_ + 1, MOD - 2, MOD) % MOD) % MOD

            overL = pow(2, n, MOD)
            removerL = pow(2, n - maxCnt, MOD)
            comB = removerL * tempans

            anS = abs(overL % MOD - (comB) % MOD) % MOD

            sys.stdout.write(str(anS) + "\n")
            continue

if __name__ == "__main__":
    main()

