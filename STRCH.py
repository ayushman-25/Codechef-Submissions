for _ in range(int(input())):
    n = int(input())
    s, c = input().split()
    total   = n * (n + 1) // 2
    missing = sum([(len(i) * (len(i) + 1) // 2)for i in s.split(c)])
    print(total - missing)