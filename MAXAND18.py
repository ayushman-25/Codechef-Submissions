for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    templ = []
    for i in arr:
        templ.append('0' * (30 - len(bin(i)[2:])) + bin(i)[2:])
    contribution = [0] * 30
    cb = [0] * 30
    # print(templ)
    for i in range(30):
        temp = 0
        for j in templ:
            if j[i] == '1':
                temp += 1
        cb[i] += temp
    for i in range(29, -1, -1):
        contribution[i] = ((1 << (30 - i - 1)) * cb[i])
    # print(contribution)
    gain = []
    for i in range(30):
        gain.append((contribution[i], 30 - i - 1))
    gain.sort(key=lambda x: x[0])
    # print(gain)
    ans = 0
    for i in range(k):
        ans += (1 << gain[30 - k][1])
    print(ans)
