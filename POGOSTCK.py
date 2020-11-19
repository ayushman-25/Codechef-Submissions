for _ in range(int(input())):
    n, step = map(int, input().split())
    arr = [int(i) for i in input().split()]
    idds = [i for i in range(0, n - step)]
    sums = [-(int(1e9) + 69)] * n
    sums += arr[n - step: ]
    modfied_ids = []
    idd = 0
    for i in range(n):
        modfied_ids.append(idd)
        idd += 1
        if (idd == step):
            idd = 0
    for i in range(n):
        temp = max(sums[modfied_ids[i]], sums[modfied_ids[i]] + arr[i])
        if temp < arr[i]:
            sums[modfied_ids[i]] = arr[i]
        else:
            sums[modfied_ids[i]] += arr[i]
    print(max(sums))