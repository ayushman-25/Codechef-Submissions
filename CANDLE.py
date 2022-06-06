for _ in range(int(input())):
    a = list(map(int, input().split()))
    minimum = min(a)
    if a[0] == minimum and a.count(minimum) == 1:
        output = "1"
        for i in range(a[0] + 1):
            output += "0"
    else:
        output = ""
        min_index = a[1: ].index(minimum)+1
        for i in range(minimum + 1):
            output += str(min_index)
    print(output)