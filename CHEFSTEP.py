for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = ''
    arr = [int(i) for i in input().split()]
    for i in arr:
        if i % k == 0:
            ans += '1'
        else:
            ans += '0'
    print(ans)