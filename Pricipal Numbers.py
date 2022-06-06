n = int(input())
arr = [int(input()) for _ in range(n)]
for i in range(n):
    try: max_pf = max([k for k in range(arr[j] - 1, 0, -1) if not (arr[j] % k)][0] for j in range(i + 1, n))
    except ValueError: max_pf = 0
    if [j for j in range(arr[i] - 1, 0, -1) if not (arr[i] % j)][0] >= max_pf:
        print(arr[i])
