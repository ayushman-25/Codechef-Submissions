'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
from math import floor, ceil
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

def g(n):
    n |= n >> 1; n |= n >> 2
    n |= n >> 4; n |= n >> 8
    n |= n >> 16; n += 1
    return(n >> 1)

mod = 998244353
def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            curr = 0
            arr = a[i:j]
            # print(arr)
            if(j == i + 1):
                print(arr)
                print(arr[0])
                ans = (ans % mod + arr[0] % mod) % mod
            else:
                arr.sort(reverse=True)
                larr = len(arr)
                if(larr == 2):
                    print(arr)
                    print(g(arr[0] ^ arr[1]))
                    ans = (ans % mod + g(arr[0] ^ arr[1]) % mod) % mod
                else:
                    cnt = 0
                    for i in arr:
                        if(floor(i ** (1 / 2)) == ceil(i ** (1 / 2))):
                            cnt += 1
                    # print(cnt)
                    start = 0
                    while(True):
                        if(cnt == 1 or start == larr):
                            break
                        if(floor(arr[start] ** (1 / 2)) == ceil(arr[start] ** (1 / 2))):
                            cnt -= 1
                            larr -= 1
                            del arr[start]
                        start += 1
                    print(arr)
                    while(True):
                        if(larr == 1):
                            break
                        temp = g(arr[0] ^ arr[1])
                        arr[1] = temp
                        del arr[0]
                        larr -= 1
                        curr += temp
                        ans = (ans % mod + temp % mod) % mod
                    print(temp)
    print(ans)




if __name__ == "__main__":
    main()
