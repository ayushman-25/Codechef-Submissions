'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
import bisect
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
        arr = [int(i) for i in input().split()]
        if (k >= max(arr)):
            print(n)
            continue
        arr.sort()
        maxarr, minarr = arr[-1], arr[0]
        if (k <= minarr):
            days = 0
            meds = k
            temparr = arr
            start = 0
            while (True):
                if (temparr[-1] == 0):
                    break
                if meds >= arr[start]:
                    meds = arr[start]
                    arr[start] = 0
                    start += 1
                    meds *= 2
                    days += 1
                else:
                    days += 1
                    meds *= 2
            print(days)
            continue
        days = bisect.bisect_left(arr, k)
        td1, td2 = 0, 1
        tempk = k
        while(1):
            if tempk >= arr[days]:
                td1 += 1
                break
            else:
                td1 += 1
                tempk *= 2
        tempk = arr[days - 1] * 2
        while(1):
            if tempk >= arr[days]:
                td2 += 1
                break
            else:
                td2 += 1
                tempk *= 2
        if(td2 <= td1):
            days -= 1
        # if(arr[days - 1] * 2 >= arr[days]) and (k != arr[days]):
        #     days -= 1
        # if(arr[days] % arr[days - 1] == 0) and (arr[days] // arr[days - 1] > 2) and (arr[days] != 1 and arr[days - 1] != 1):
        #     days -= 1
        left_pop = arr[days:]
        start = 0
        meds = k
        while (True):
            if (left_pop[-1] == 0):
                break
            if meds >= left_pop[start]:
                meds = left_pop[start]
                left_pop[start] = 0
                start += 1
                meds *= 2
                days += 1
            else:
                days += 1
                meds *= 2
        print(days)

if __name__ == "__main__":
    main()
