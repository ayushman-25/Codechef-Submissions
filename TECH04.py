for _ in range(int(input())):
    a, b = input().split()
    arr = [0] * 26
    c = 0
    for i in range(len(a)):
        arr[ord(a[i]) - ord('a')] += 1
    for i in range(len(b)):
        arr[ord(b[i]) - ord('a')] -= 1
    for i in arr:
        c += abs(i)
    if c == 0:
        print("YES")
    else:
        print("NO")