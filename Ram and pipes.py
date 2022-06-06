from heapq import heapify, heappop, heappush
arr = [int(input()) for _ in range(int(input()))]
heapify(arr)
ans = 0 if (len(arr) > 1) else arr[0]
while len(arr) > 1:
    val = heappop(arr) + heappop(arr)
    heappush(arr, val); ans += val
print(ans)
