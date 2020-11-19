'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
# from math import gcd
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


# gfg reference
def fun(n):
    if(n < 2):
        return 0
    res, k = 1, 2
    if(k > n - k):
        k = n - k
    for i in range(0, k):
        res *= (n - i)
        res = int(res / (i + 1))
    return res

def sum(n):
    return n * (n + 1) // 2

def main():
    for _ in range(int(input())):
        n = int(input())
        if(n % 4 == 1 or n % 4 == 2):
            print(0)
            continue
        full = sum(n)
        tS = n * (n + 1) // 4
        low, high = 1, n
        while(1):
            mid = low + (high - low) // 2
            if(full - sum(mid) < tS): high = mid - 1
            elif(full - sum(mid) == tS):
                ans = n - mid
                print(ans + fun(ans) + fun(mid))
                break
            else:
                if(full - sum(mid + 1) < tS):
                    print(n - mid)
                    break
                else:
                    low = mid + 1

if __name__ == "__main__":
    main()


# '''
#
# * Author : Ayushman Chahar #
# * About  : II Year, IT Undergrad #
# * Insti  : VIT, Vellore #
#
# '''
#
# import os
# import sys
# from io import BytesIO, IOBase
#
# # BUFSIZE = 8192
# #
# #
# # class FastIO(IOBase):
# #     newlines = 0
# #
# #     def __init__(self, file):
# #         self._fd = file.fileno()
# #         self.buffer = BytesIO()
# #         self.writable = "x" in file.mode or "r" not in file.mode
# #         self.write = self.buffer.write if self.writable else None
# #
# #     def read(self):
# #         while True:
# #             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
# #             if not b:
# #                 break
# #             ptr = self.buffer.tell()
# #             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
# #         self.newlines = 0
# #         return self.buffer.read()
# #
# #     def readline(self):
# #         while self.newlines == 0:
# #             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
# #             self.newlines = b.count(b"\n") + (not b)
# #             ptr = self.buffer.tell()
# #             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
# #         self.newlines -= 1
# #         return self.buffer.readline()
# #
# #     def flush(self):
# #         if self.writable:
# #             os.write(self._fd, self.buffer.getvalue())
# #             self.buffer.truncate(0), self.buffer.seek(0)
# #
# #
# # class IOWrapper(IOBase):
# #     def __init__(self, file):
# #         self.buffer = FastIO(file)
# #         self.flush = self.buffer.flush
# #         self.writable = self.buffer.writable
# #         self.write = lambda s: self.buffer.write(s.encode("ascii"))
# #         self.read = lambda: self.buffer.read().decode("ascii")
# #         self.readline = lambda: self.buffer.readline().decode("ascii")
# #
# #
# # sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")
#
#
# def main():
#     for _ in range(int(input())):
#         n = int(input())
#         if(n % 4 == 1 or n % 4 == 2):
#             print(0)
#             continue
#         full = (n * (n + 1) // 2)
#         arr = [i for i in range(1, n + 1)]
#         # tP = n - int(n ** (1 / 2)) - 2
#         ans = 0
#         for i in range(n):  # accessing the first element of our pair
#             # if(i == tP):
#             #     tP += 1
#             for j in range(i + 1, n):
#                 t1 = arr[i]
#                 t2 = arr[j]
#                 arr[i] = t2
#                 arr[j] = t1
#                 # for x in range(n):
#                 #     print(arr[x], end=' ')
#                 # print()
#                 # print('1',arr)
#                 for k in range(n // 2 - 1, n - 1):
#                     neededS = (k + 1) * (k + 2) // 2
#                     # print("Brute: ", sum(arr[0: k + 1]), sum(arr[k + 1:]))
#                     if(i <= k and j <= k):
#                         # no need to update the sums
#                         # print("Optimal: ", sumstore[k], (tS - sumstore[k]), 'if')
#                         if(neededS == (full - neededS)):
#                             print((arr[0: k + 1]), (arr[k + 1:]))
#                             print('sum: ', neededS)
#                             print('swap ith', i + 1, j + 1)
#                             print('k: ', k + 1)
#                             # print(k)
#                             ans += 1
#                     elif(i <= k and j > k):
#                         temp1 = neededS
#                         # print('x', temp1, arr[i], arr[j])
#                         temp1 -= t1
#                         temp1 += t2
#                         # print(temp1)
#                         temp2 = full - neededS
#                         # print('y', temp2)
#                         temp2 -= t2
#                         temp2 += t1
#                         # print(temp2)
#                         # print("Optimal: ", temp1, temp2, 'elif')
#                         if(temp1 == temp2):
#                             print((arr[0: k + 1]), (arr[k + 1:]))
#                             print('sum: ', temp1)
#                             print('swap ith', i + 1, j + 1)
#                             print('k: ', k + 1)
#                             # print(k)
#                             ans += 1
#                         # need to update the sum
#                     else:
#                         # no need to update as both i, j lie in last segment
#                         # print("Optimal: ", sumstore[k], (tS - sumstore[k]), 'else')
#                         if(neededS == (full - neededS)):
#                             print((arr[0: k + 1]), (arr[k + 1:]))
#                             print('sum: ', neededS)
#                             print('swap ith', i + 1, j + 1)
#                             print('k: ', k + 1)
#                             # print(k)
#                             ans += 1
#                     # if(sum(arr[0: k + 1]) == sum(arr[k + 1: ])):
#                     #     print(arr[0: k + 1], arr[k + 1: ])
#                     #     ans += 1
#                 arr[i] = t1
#                 arr[j] = t2
#         print(n, ans)
#
# if __name__ == "__main__":
#     main()
