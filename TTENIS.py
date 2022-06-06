'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
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
        s = input()
        chef, chefu = 0, 0
        start = 0
        exception = False
        while(True):
            # print(chef, chefu)
            # print(start, "match")
            if(((chef < chefu and chefu > 10) or (chef > chefu and chef > 10)) and not exception):
                if(chef >= 11):
                    print("WIN")
                    break
                else:
                    print("LOSE")
                    break
            if(chef == chefu == 10):
                exception = True
            if(exception):
                if(chef + 2 == chefu):
                    print("LOSE")
                    break
                elif(chef == chefu + 2):
                    print("WIN")
                    break
            if(s[start] == '1'): chef += 1
            elif(s[start] == '0'): chefu += 1
            start += 1

############################################
###################OR########################
        print("LOSE" if s.count('0') > s.count('1') else "WIN")

if __name__ == "__main__":
    main()
