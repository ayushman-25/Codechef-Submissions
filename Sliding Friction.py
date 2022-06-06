n, arr = int(input()), list(map(int, input().split()))
m = a1 = a2 = 0
for i in range(n):
    for j in range(i + 1, n):
        check = arr[i: j + 1]
        if sorted(check) == check and len(check) == len(set(check)) and len(check) > m:
            if len(check) > m:
                m = len(check)
                a1, a2 = i, j
print(a1 + 1, a2 + 1)

