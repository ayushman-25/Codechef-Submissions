n = int(input())
arr = [int(input()) for _ in range(n)]
q = int(input())
time, iter = [0 for _ in range(n)], 0
while sum(arr):
    x = arr[iter] if arr[iter] <= q else q
    for i in range(n):
        time[i] += x if arr[i] else 0
    arr[iter] -= x
    iter += 1 if iter < n - 1 else -iter
print(*time, sep='\n')
