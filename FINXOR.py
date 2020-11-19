'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''


# import os
# import sys
# from io import BytesIO, IOBase

# BUFSIZE = 8192
#
#
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


def main():
    for _ in range(int(input())):

        total = int(input())
        xs = []

        for i in range(1, 21):
            # try to ask query for each bit, <= 20
            print(1, 1 << i, flush=True)
            x = int(input())
            if (x == -1): exit(0)
            xs.insert(0, x)

        # set the initial sum as abs((N * (1 << 20)) - xs[::-1][0]);
        sM = xs[0]
        sM -= (total * (1 << 20))

        xor = 0
        if (sM & 1): xor = 1
        # print(sM)
        # sM = abs((N * (1 << 20)) - xs[::-1][0])

        status = [0] * 20

        # range over each bit
        for i in range(1, 21 - 1):
            if (xs[i] < sM):
                xs[i] = ((total + abs(xs[i] - sM) // (1 << abs(i - 20))) // 2)
                if (xs[i] & 1): status[i] = 1
            else:
                xs[i] = ((total - abs(sM - xs[i]) // (1 << abs(i - 20))) // 2)
                if (xs[i] & 1): status[i] = 1

        # for i in xs:
        #     print(i)


        for i in range(1, 21 - 1):
            if (status[i] & 1): xor += (1 << abs(i - 20))

        # print(xor)
        # for i in xs:
        #     print(i)

        print(2, xor, flush=True)

        correct = int(input())
        if (correct == -1): exit(0)


if __name__ == "__main__":
    main()

## BRUTE FORCE
# from collections import Counter
# # arr = [1, 3, 7, 10, 11]
# arr = [1, 3, 7, 10, 11, 113]
# binaries = [bin(i)[2: ] for i in arr]
# print(*arr)
# print(*binaries)
# summation = sum(arr)
# xor = 0
#
# for i in arr:
#     xor ^= i
# print("xor: ", xor)
# temp1 = []
# # temp2 = []
#
# tempr = [1 << i for i in range(1, 21)]
# for i in tempr:
#     ans = 0
#     for j in range(len(arr)):
#         ans += (arr[j] ^ i)
#     temp1.append(ans)
#     # temp2.append(summation ^ i)
#     print('i: ', i, ' ', ans, 'bin: ', bin(ans)[2: ])
# print(temp1)
# for i in temp1:
#     print(i)
# print(temp2)
# t = Counter(temp1).most_common(len(temp11))
# # print('elem ', t[0][0])
# # print('cnt ', t[0][1])
# print(Counter(temp))


# for _ in range(int(input())):
#     n = int(input())
#     # now start asking queries using 1 and answer as 2
#     print(1, )
#     ans = int(input())