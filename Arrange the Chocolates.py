n = int(input())
arr = sorted(list(map(int, input().split())))
ans = list()
l, r = 0, len(arr) - 1
while l <= r:
    ans.append(arr[l])
    ans.append(arr[r])
    l += 1
    r -= 1
print(*ans)
sm = sum(arr[i] - arr[j] for i in range(len(arr) - 1) for j in range(len(arr) - 1))
