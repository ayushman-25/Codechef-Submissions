for _ in range(int(input())):
    dict1 = {}
    for y in range(int(input())):
        a, b=input().split()
        if b == '+':
            dict1[a] = 1
        else:
            dict1[a] = -1
    print(sum(dict1.values()))