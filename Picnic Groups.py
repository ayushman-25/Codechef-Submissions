for _ in range(int(input())):
    n, arr, ans = int(input()), sorted(list(map(int, input().split()))), 0
    while (len(arr) > 1):
        check = arr[0] + arr[-1]
        if (check < 4): arr.append(arr.pop(0) + arr.pop(-1)); continue
        ans += check >= 4
        arr.pop(-1)
        if (check == 4): arr.pop(0)
    print(ans + bool(arr))
