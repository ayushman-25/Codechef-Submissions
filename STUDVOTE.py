for __ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    s = set()
    c = 0
    for i in range(1, n + 1):
        if i == arr[i - 1]:
            s.add(arr[i - 1])
    for i in range(1, n + 1):
        if arr.count(i) >= k and i not in s:
            c += 1
    print(c)