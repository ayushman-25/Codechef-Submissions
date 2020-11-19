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


mod = int(1e9) + 7

def solve():
    n = readint()
    arr = readarri()
    q = readint()
    if(n <= 10):
        for _ in range(q):
            r = readint()
            chef, chefu = 0, 0
            if (1 not in arr):  # chefu ko kuch milega hee nahi isme, *anda*
                if (r == 1): print(arr[0] % mod); continue
                # if (r == 2): print((arr[0] % mod + arr[1 % n] % mod) % mod); continue
                i = 0
                while (1):
                    idx = i % n
                    if (i == r - 2):
                        if ((idx + 1) % n != 0):
                            if (arr[idx] & 1):
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            else:
                                chef = (chef % mod + arr[idx] % mod) % mod
                        else:
                            if (arr[idx] & 1):
                                chef = (chef % mod + arr[idx] % mod) % mod
                            else:
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod)
                        chef = (chef % mod + arr[(i + 1) % n] % mod) % mod
                        break
                    if ((idx + 1) % n == 0):
                        if (arr[idx] & 1):
                            chef = (chef % mod + arr[idx] % mod) % mod
                        else:
                            chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                        i += 1
                        continue
                    if (arr[idx] & 1):
                        chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod)
                    else:
                        chef = (chef % mod + arr[idx] % mod) % mod
                    i += 1
                print(chef % mod)
            else:
                if (arr.index(1) == n - 1):
                    if (r == 1): print(arr[0] % mod); continue
                    # if (r == 2): print((arr[0] % mod + arr[1 % n] % mod) % mod); continue
                    i = 0
                    while (1):
                        idx = i % n
                        # print(chef)
                        if (i == r - 2):
                            if ((idx + 1) % n != 0):
                                if (arr[idx] & 1):
                                    chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                else:
                                    chef = (chef % mod + arr[idx] % mod) % mod
                            else:
                                if (arr[idx] & 1):
                                    chef = (chef % mod + arr[idx] % mod) % mod
                                else:
                                    chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod)
                            chef = (chef % mod + arr[(i + 1) % n] % mod) % mod
                            break
                        if ((idx + 1) % n == 0):
                            if (arr[idx] & 1):
                                chef = (chef % mod + arr[idx] % mod) % mod
                            else:
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            i += 1
                            continue
                        if (arr[idx] & 1):
                            chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod)
                        else:
                            chef = (chef % mod + arr[idx] % mod) % mod
                        i += 1
                    print(chef % mod)
                elif (0 < arr.index(1) < n - 1):
                    if (r == 1): print(arr[0] % mod); continue
                    # if (r == 2): print((arr[0] % mod + arr[1 % n] % mod) % mod); continue
                    i = 0
                    while (1):
                        # print(chef)
                        idx = i % n
                        if (i == r - 2):
                            if ((idx + 1) % n != 0):
                                if (arr[idx] & 1):
                                    chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                else:
                                    chef = (chef % mod + arr[idx] % mod) % mod
                            else:
                                if (arr[idx] & 1):
                                    chef = (chef % mod + arr[idx] % mod) % mod
                                else:
                                    chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            chef = (chef % mod + arr[(i + 1) % n] % mod) % mod
                            break
                        if ((idx + 1) % n == 0):
                            if (arr[idx] & 1):
                                chef = (chef % mod + arr[idx] % mod) % mod
                            else:
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            i += 1
                            continue
                        if (arr[idx + 1] == 1):
                            if (arr[idx] & 1):
                                chef = (chef % mod + arr[idx] % mod) % mod
                            else:
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            i += 1
                            continue
                        if (arr[idx] & 1):
                            chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                        else:
                            chef = (chef % mod + arr[idx] % mod) % mod
                        i += 1
                    print(chef % mod)
                else:
                    # now here comes the catchy part
                    # as now its chance of the chefu to play optimally and beat the hell out of chef
                    chef += 1  # getting the first candy according to the condition
                    if (r == 1): print(arr[0] % mod); continue
                    if (r == 2): print(arr[0] % mod); continue
                    i = 1
                    while (1):
                        # print(chef, i)
                        idx = i % n
                        if (i == r - 2):
                            if ((idx + 1) % n != 0):
                                if (arr[idx] & 1):
                                    chefu = (chefu % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                else:
                                    chefu = (chefu % mod + arr[idx] % mod) % mod
                            else:
                                if (arr[idx] & 1):
                                    chefu = (chefu % mod + arr[idx] % mod) % mod
                                else:
                                    chefu = (chefu % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            chefu = (chefu % mod + arr[(i + 1) % n] % mod) % mod
                            break
                        if ((idx + 1) % n == 0):
                            if (arr[idx] & 1):
                                chefu = (chefu % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                i += 1
                            else:
                                chefu = (chefu % mod + arr[idx] % mod) % mod
                                i += 1
                            idx = i % n
                            chef = (chef % mod + arr[idx] % mod) % mod
                            # i += 1    GAME CHANGING COMMENT
                            continue
                        if (arr[idx] & 1):
                            chefu = (chefu % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                        else:
                            chefu = (chefu % mod + arr[idx] % mod) % mod
                        i += 1
                    print(chef % mod)
    else:
        if(1 not in arr):
            preC = []
            tot = 0
            if(n >= 2):
                i = 0
                while(1):
                    if(i == n): break
                    if(i == n - 1):
                        if(arr[i] & 1):
                            tot = (tot % mod + arr[i] % mod) % mod
                        else:
                            tot = (tot % mod + (arr[i] % mod - 1 % mod) % mod) % mod
                        i += 1
                        continue
                    if(arr[i] & 1):
                        tot = (tot % mod + (arr[i] % mod - 1 % mod) % mod) % mod
                    else:
                        tot = (tot % mod + arr[i] % mod) % mod
                    i += 1
                # now lets fucking work with the precomputations and shit
                i, chef, r = 0, 0, n
                while (1):
                    idx = i % n
                    if (i == r - 2):
                        if ((idx + 1) % n != 0):
                            if (arr[idx] & 1):
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                preC.append((chef % mod + 1 % mod) % mod)
                            else:
                                chef = (chef % mod + arr[idx] % mod) % mod
                                preC.append(chef % mod)
                        else:
                            if (arr[idx] & 1):
                                chef = (chef % mod + arr[idx] % mod) % mod
                                preC.append(chef % mod)
                            else:
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod)
                                preC.append((chef % mod + 1 % mod) % mod)
                        chef = (chef % mod + arr[(i + 1) % n] % mod) % mod
                        preC.append(chef % mod)
                        break
                    if ((idx + 1) % n == 0):
                        if (arr[idx] & 1):
                            chef = (chef % mod + arr[idx] % mod) % mod
                            preC.append(chef % mod)
                        else:
                            chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            preC.append((chef % mod + 1 % mod) % mod)
                        i += 1
                        continue
                    if (arr[idx] & 1):
                        chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                        preC.append((chef % mod + 1 % mod) % mod)
                    else:
                        chef = (chef % mod + arr[idx] % mod) % mod
                        preC.append(chef % mod)
                    i += 1
            else:
                if(n == 1):
                    preC = [arr[0]]
                    tot = preC[0]
                # elif(n == 2):
                #     preC = [arr[0], arr[0] + arr[1]]
                #     tot = preC[1]
            for _ in range(q):
                chef = 0
                r = readint()
                R = r
                if(n == 1):
                    if(r == 1):
                        print(arr[0] % mod)
                    else:
                        if(not(arr[0] & 1)):
                            temp = ((arr[0] % mod - 1 % mod) % mod * (r % mod - 1 % mod) % mod) % mod
                        else:
                            temp = ((arr[0] % mod - 0 % mod) % mod * (r % mod - 1 % mod) % mod) % mod
                        print((arr[0] % mod + temp % mod) % mod)
                    continue
                if(r <= n):
                    print(preC[r - 1] % mod)
                else:
                    if(r / n == r // n):
                        tp = r // n - 1
                        r %= n
                        chef = (chef % mod + (tot % mod * tp % mod) % mod) % mod
                        chef = (chef % mod + preC[r - 1] % mod) % mod
                    else:
                        tp = r // n
                        r %= n
                        chef = (chef % mod + (tot % mod * tp % mod) % mod) % mod
                        chef = (chef % mod + preC[r - 1] % mod) % mod
                    print(chef % mod)
        else:
            fnd = arr.index(1)
            # print("fnd", fnd)
            if(fnd == n - 1):
                preC = []
                tot = 0
                if(n >= 2):
                    i = 0
                    while(1):
                        if(i == n):
                            break
                        if(i == n - 1):
                            if(arr[i] & 1):
                                tot = (tot % mod + arr[i] % mod) % mod
                            else:
                                tot = (tot % mod + (arr[i] % mod - 1 % mod) % mod) % mod
                            i += 1
                            continue
                        if(arr[i] & 1):
                            tot = (tot % mod + (arr[i] % mod - 1 % mod) % mod) % mod
                        else:
                            tot = (tot % mod + arr[i] % mod) % mod
                        i += 1
                    # print(tot)
                    # start calculating precomputations
                    i, chef, r = 0, 0, n
                    while (1):
                        idx = i % n
                        # print(chef)
                        if (i == r - 2):
                            if ((idx + 1) % n != 0):
                                if (arr[idx] & 1):
                                    chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                    preC.append((chef % mod + 1 % mod) % mod)
                                else:
                                    chef = (chef % mod + arr[idx] % mod) % mod
                                    preC.append(chef % mod)
                            else:
                                if (arr[idx] & 1):
                                    chef = (chef % mod + arr[idx] % mod) % mod
                                    preC.append(chef % mod)
                                else:
                                    chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                    preC.append((chef % mod + 1 % mod) % mod)
                            chef = (chef % mod + arr[(i + 1) % n] % mod) % mod
                            preC.append(chef % mod)
                            break
                        if ((idx + 1) % n == 0):
                            if (arr[idx] & 1):
                                chef = (chef % mod + arr[idx] % mod) % mod
                                preC.append(chef % mod)
                            else:
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                preC.append((chef % mod + 1 % mod) % mod)
                            i += 1
                            continue
                        if (arr[idx] & 1):
                            chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            preC.append((chef % mod + 1 % mod) % mod)
                        else:
                            chef = (chef % mod + arr[idx] % mod) % mod
                            preC.append(chef % mod)
                        i += 1
                else:
                    if(n == 1):
                        preC = [arr[0]]
                        tot = preC[0]
                    # elif(n == 2):
                    #     preC = [arr[0], arr[0] + arr[1]]
                    #     tot = preC[1]
                # print(preC)
                for _ in range(q):
                    chef = 0
                    r = readint()
                    if (n == 1):
                        if (r == 1):
                            print(arr[0] % mod)
                        else:
                            if (not(arr[0] & 1)):
                                temp = ((arr[0] % mod - 1 % mod) % mod * (r % mod - 1 % mod) % mod) % mod
                            else:
                                temp = ((arr[0] % mod - 0 % mod) % mod * (r % mod - 1 % mod) % mod) % mod
                            print((arr[0] % mod + temp % mod) % mod)
                        continue
                    if (r <= n):
                        print(preC[r - 1] % mod)
                    else:
                        if (r / n == r // n):
                            tp = r // n - 1
                            r %= n
                            chef = (chef % mod + (tot % mod * tp % mod) % mod) % mod
                            chef = (chef % mod + preC[r - 1] % mod) % mod
                        else:
                            tp = r // n
                            r %= n
                            chef = (chef % mod + (tot % mod * tp % mod) % mod) % mod
                            chef = (chef % mod + preC[r - 1] % mod) % mod
                        print(chef % mod)
            elif(0 < fnd < n - 1):
                preC = []
                tot = 0
                if(n >= 2):
                    i = 0
                    while(1):
                        if(i == n):
                            break
                        if(i == n - 1):
                            if(arr[i] & 1):
                                tot = (tot % mod + arr[i] % mod) % mod
                                i += 1
                            else:
                                tot = (tot % mod + (arr[i] % mod - 1 % mod) % mod) % mod
                                i += 1
                            continue
                        if(arr[i + 1] == 1):
                            if(arr[i] & 1):
                                tot = (tot % mod + arr[i] % mod) % mod
                                i += 1
                            else:
                                tot = (tot % mod + (arr[i] % mod - 1 % mod) % mod) % mod
                                i += 1
                            continue
                        if(arr[i] & 1):
                            tot = (tot % mod + (arr[i] % mod - 1 % mod) % mod) % mod
                        else:
                            tot = (tot % mod + arr[i] % mod) % mod
                        i += 1
                    # print(tot)
                    # start calculating precomputations
                    i, chef, r = 0, 0, n
                    while (1):
                        # print(chef)
                        idx = i % n
                        if (i == r - 2):
                            if ((idx + 1) % n != 0):
                                if (arr[idx] & 1):
                                    chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                    preC.append((chef % mod + 1 % mod) % mod)
                                else:
                                    chef = (chef % mod + arr[idx] % mod) % mod
                                    preC.append(chef % mod)
                            else:
                                if (arr[idx] & 1):
                                    chef = (chef % mod + arr[idx] % mod) % mod
                                    preC.append(chef % mod)
                                else:
                                    chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                    preC.append((chef % mod + 1 % mod) % mod)
                            chef = (chef % mod + arr[(i + 1) % n] % mod) % mod
                            preC.append(chef % mod)
                            break
                        if ((idx + 1) % n == 0):
                            if (arr[idx] & 1):
                                chef = (chef % mod + arr[idx] % mod) % mod
                                preC.append(chef % mod)
                            else:
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                preC.append((chef % mod + 1 % mod) % mod)
                            i += 1
                            continue
                        if (arr[idx + 1] == 1):
                            if (arr[idx] & 1):
                                chef = (chef % mod + arr[idx] % mod) % mod
                                preC.append(chef % mod)
                            else:
                                # print(chef)
                                preC.append((chef % mod + arr[idx] % mod) % mod)
                                chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                                # print(chef)
                                # preC.append((chef % mod + 1 % mod) % mod)
                            i += 1
                            continue
                        if (arr[idx] == 1):
                            # print("entered", arr[idx - 1], idx, chef)
                            if(not(arr[idx - 1] & 1)):
                                # print(arr[idx - 1], 'prev')
                                preC.append(((chef % mod + 1 % mod) % mod + arr[idx] % mod) % mod)
                            else:
                                preC.append(chef % mod)
                            i += 1
                            continue
                        if (arr[idx] & 1):
                            # print(chef, arr[idx], 'asdads')
                            preC.append((chef % mod + arr[idx] % mod) % mod)
                            chef = (chef % mod + (arr[idx] % mod - 1 % mod) % mod) % mod
                            # print((chef % mod + 1 % mod) % mod)
                            # preC.append((chef % mod + 1 % mod) % mod)
                        else:
                            # print(arr[idx], chef)
                            chef = (chef % mod + arr[idx] % mod) % mod
                            preC.append(chef % mod)
                        i += 1
                else:
                    if(n == 1):
                        preC = [arr[0]]
                        tot = preC[0]
                    # elif(n == 2):
                    #     preC = [arr[0], arr[0] + arr[1]]
                    #     tot = preC[1]
                # print(preC)
                for _ in range(q):
                    chef = 0
                    r = readint()
                    if (n == 1):
                        if (r == 1):
                            print(arr[0] % mod)
                        else:
                            if (not(arr[0] & 1)):
                                temp = ((arr[0] % mod - 1 % mod) % mod * (r % mod - 1 % mod) % mod) % mod
                            else:
                                temp = ((arr[0] % mod - 0 % mod) % mod * (r % mod - 1 % mod) % mod) % mod
                            print((arr[0] % mod + temp % mod) % mod)
                        continue
                    if (r <= n):
                        print(preC[r - 1] % mod)
                    else:
                        if (r / n == r // n):
                            tp = r // n - 1
                            r %= n
                            chef = (chef % mod + (tot % mod * tp % mod) % mod) % mod
                            chef = (chef % mod + preC[r - 1] % mod) % mod
                        else:
                            tp = r // n
                            r %= n
                            chef = (chef % mod + (tot % mod * tp % mod) % mod) % mod
                            chef = (chef % mod + preC[r - 1] % mod) % mod
                        print(chef % mod)
            else:
                for _ in range(q):
                    r = readint()
                    if(r <= n):
                        print(1)
                        continue
                    tp = r // n
                    if(r % n == 0):
                        print((tp % mod * 1 % mod) % mod)
                        continue
                    if(r % n == 1):
                        print((tp % mod * 1 % mod) % mod)
                    else:
                        print(((tp % mod + 1 % mod) % mod * 1 % mod) % mod)


def main():
    for _ in range(readint()):
        # print("CANDY")
        solve()



if __name__ == "__main__":
    main()
