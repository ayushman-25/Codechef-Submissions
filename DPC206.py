for _ in range(int(input())):
    n = input()
    c = 0
    while(n != n[::-1]):
        z = int(n) + int(n[::-1])
        n = str(z)
        c = c + 1
    print(c, int(n))
