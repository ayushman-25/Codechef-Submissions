for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    if(k >= n):
        print(s)
    else:
        myans = s[:k]
        rem = n - k
        start = 0

        while(rem > 0):
            myans += s[start]
            start += 1
            if(start == k):
                start = 0
            rem -= 1
        print(myans)