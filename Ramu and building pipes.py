from heapq import heapify, heappop, heappush

f, h, d, n, ans = int(input()), int(input()), int(input()), int(input()), 0
arr = [int(input()) for _ in range(n * 2)]
arr = [arr[i + 1] for i in range(0, (n * 2) - 1, 2) if (arr[i] == d)]
heapify(arr)
while len(arr) > 1:
    val = heappop(arr) + heappop(arr)
    heappush(arr, val)
    ans += val
print(ans)
