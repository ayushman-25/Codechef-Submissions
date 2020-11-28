n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
start = int(input())
for i in range(n):
    if(arr[i][0] == start):
        last, size = arr[i], 1
        for j in range(i + 1, n):
            if(arr[j][0] == last[1] and arr[j][1] == start):
                print(size + 1)
                exit(0)
            if(arr[j][0] == last[1]):
                last = arr[j]
                size += 1
print(0)