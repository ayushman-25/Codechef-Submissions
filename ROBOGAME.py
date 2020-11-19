for _ in range(int(input())):
    s = input()
    ranges = []
    for ch, i in enumerate(s):
        if i != '.':
            ranges.append([ch - int(i), ch + int(i)])
    ranges.sort()
    safe = True
    lr = len(ranges)
    if(lr == 1):
        print("safe")
        continue
    for i in range(1, lr):
        if ranges[i][0] <= ranges[i - 1][1]:
            safe = False
            break
    print("safe" if safe else "unsafe")

