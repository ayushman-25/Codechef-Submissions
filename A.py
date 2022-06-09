"""

* Author : Ayushman Chahar
* About  : IT, Senior

"""

import os, sys
from collections import defaultdict
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

start = 0
mersenne = list()
while 1:
    if 2 ** start - 1 > 1073741824:
        break
    mersenne.append(2 ** start - 1)
    start += 1



def brute(n, k, my_ans):




def solve():
    n, k = readints()
    if k <= n:
        print(k); return
    ans = 0
    for i in range(len(mersenne)):
        store = defaultdict(int)
        spaces_left = n
        if n * mersenne[i] < k:
            continue
        elif n * mersenne[i] == k:
            ans = max(ans, n * bin(mersenne[i]).count('1'))
        start = i
        orig_k = k
        while 1:
            if spaces_left == 0:
                break
            if mersenne[start] == 0:
                store[0] = spaces_left
                spaces_left = 0
                continue
            store[mersenne[start]] = k // mersenne[start]
            spaces_left -= k // mersenne[start]
            k -= k // mersenne[start] * mersenne[start]
            start -= 1
        k = orig_k
        ans = max(ans, sum([store[i] * bin(i).count('1') for i in store.keys()]))
        if mersenne[i] > k:
            break
    for po in range(0, 35):
        po = 2 ** po - 1
        hmm = k - po * (n - 1)
        if hmm >= 0:
            ans = max(ans, ((n - 1) * bin(po).count('1') + bin(hmm).count('1')))
    print(ans)


def main():
    t = 1
    t = readint()
    for _ in range(t):
        # print("Case #" + str(_ + 1) + ": ", end="")
        solve()


if __name__ == "__main__":
    main()
