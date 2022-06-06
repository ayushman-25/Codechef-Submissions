# Author - Ayushman Chahar
import sys
n, q = map(int, sys.stdin.readline().split())
myArr = [0] * n
myDiffArr = [0] * (n + 1)
for i in range(q):
    a, b, c = map(int, sys.stdin.readline().split())
    # myDiffArr[a - 1] += c
    # myDiffArr[b] -= c
    for j in range(a - 1, b):
        myArr[j] += c
    print(myArr)
# for i in range(n):
    # if(i == 0):
        # myArr[i] = myDiffArr[i]
    # else:
        # myArr[i] = myDiffArr[i] + myArr[i - 1]
for _ in range(int(sys.stdin.readline())):
    sys.stdout.write(str(myArr[int(sys.stdin.readline()) - 1]) + '\n')