from heapq import *

n = int(input())
arr = [int(input()) for _ in range(n)]
if(n == 1): print(arr[0]); exit(0)
heapify(arr)
ans = 0
while(n > 1):
    val = heappop(arr) + heappop(arr)
    heappush(arr, val)
    n -= 1
    ans += val
print(ans)