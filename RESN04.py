for _ in range(int(input())):
    res = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        res += arr[i] // (i + 1)
    if res % 2 != 0:
        print("ALICE")
    else:
        print("BOB")