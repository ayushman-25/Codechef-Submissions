n, a, c, h = int(input()), [[]], 0, 0
for i in range(n + 10):
    a[-1].append(i + 1)
    c += 1
    if c == 6:
        a.append([])
        c = 0
        a[-2] = a[-2][::-1] if h else a[-2]
        h ^= 1
for i in range(n + 10):
    for j in range(6):
        if a[i][j] == n:
            print(a[i - 1][j] if i & 1 else a[i + 1][j])
            if j == 0 or j == 5:
                print("Green")
            elif j == 1 or j == 4:
                print("Orange")
            else:
                print("Blue")
            exit(0)

