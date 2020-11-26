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


def solve():
	P = input
	J = int
	E = len
	D = range
	B = [None] * 100001
	L = []
	for A in D(2, E(B)): B[A] = set()
	for A in D(2, 100001):
		if E(B[A]) != 0: continue
		L.append(A);
		B[A].add(A)
		for F in D(2, E(B)):
			G = F * A
			if G > 100000:
				break
			else:
				while G <= 100000: B[G].add(A);G *= A
	C = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
	K = [0, 0, 0, 0, 0, 0]
	for A in D(2, E(B)):
		for F in D(1, E(C)): C[F].append(K[F])
		H = E(B[A])
		if H <= 5: C[H][-1] += 1;K[H] += 1
	M = J(P())
	for Q in D(1, M + 1): I = P().split(' ');N = J(I[0]);O = J(I[1]);type = J(I[2]);print(
		f"{C[type][O] - C[type][N - 1]}")

def main():
    # for _ in range(readint()):
	solve()


if __name__ == "__main__":
    main()
