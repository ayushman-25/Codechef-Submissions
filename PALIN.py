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
readint = lambda: int(sys.stdin.readline().rstrip("\r\n"))
readints = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split())
readstr = lambda: sys.stdin.readline().rstrip("\r\n")
readstrs = lambda: map(str, sys.stdin.readline().rstrip("\r\n").split())
readarri = lambda: [int(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]
readarrs = lambda: [str(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]


def main():
    for _ in range(readint()):
        s = readstr()
        ln = len(s)
        if ln < 2:
            st = int('0' + s) + 1
            if st == 10: print('11'); continue
            else: print(str(st)); continue
        mid = ln // 2
        mid_val = (s[mid] if ln & 1 else '')
        lblock = list(reversed(s[0:mid]))
        rblock = s[-mid:ln]
        inc_st = True
        for stc, enc in zip(lblock, rblock):
            if enc < stc: inc_st = False; break
            elif stc < enc: break
        if inc_st:
            if mid_val == '9': mid_val = '0'
            elif mid_val != '':
                mid_val = str(1 + int(mid_val))
                inc_st = False
        if inc_st:
            for ind, val in enumerate(lblock):
                if val != '9':
                    lblock[ind] = str(int(lblock[ind]) + 1)
                    inc_st = False
                    break
                else: lblock[ind] = '0'
            if inc_st:
                lblock[-1] = '1'
                mid_val += '0'
        sys.stdout.write(''.join((*reversed(lblock), mid_val, *lblock)) + "\n")

if __name__ == "__main__":
    main()
