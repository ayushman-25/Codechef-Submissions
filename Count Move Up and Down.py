n = int(input())
arr = list(map(int, input().split()))
status = 1 if (arr[1] > arr[0]) else 0
up = down = 0
for i in range(1, n - 1):
    if arr[i] > arr[i + 1] and status == 1:
        status ^= 1
        up += 1
    if arr[i] < arr[i + 1] and status == 0:
        status ^= 1
        down += 1
print(up + arr[-1] > arr[-2] and status == 1, down + arr[-1] < arr[-2] and status == 0)
