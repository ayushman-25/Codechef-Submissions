'''

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

'''

import os
import sys
from collections import defaultdict
import math
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
	left = 'df'
	right = 'jk'
	for _ in range(int(input())):
		n = int(input())
		ans = 0
		status = defaultdict(int)
		words = []
		for _ in range(n):
			s = input()
			if(s in words):
				if(len(s) == 1):
					ans += 0.1
				else:
					ans += 0.1
					last = s[0]
					for i in range(1, len(s)):
						if(s[i] in left and last in left):
							ans += 0.2
							last = s[i]
							continue
						if(s[i] in right and last in right):
							ans += 0.2
							last = s[i]
							continue
						else:
							ans += 0.1
							last = s[i]
				words.append(s)
			else:
				if (len(s) == 1):
					ans += 0.2
				else:
					ans += 0.2
					last = s[0]
					for i in range(1, len(s)):
						if (s[i] in left and last in left):
							ans += 0.4
							last = s[i]
							continue
						if (s[i] in right and last in right):
							ans += 0.4
							last = s[i]
							continue
						else:
							ans += 0.2
							last = s[i]
				words.append(s)
		print(math.ceil(ans * 10))


if __name__ == "__main__":
	main()
