for _ in range(int(input())):
    a1, a2, a3, a4, a5, p = map(int, input().split())
    tot = 24 * 5
    a1 *= p
    a2 *= p
    a3 *= p
    a4 *= p
    a5 *= p
    if((a1 + a2 + a3 + a4 + a5) <= tot):
        print("No")
    else:
        print("Yes")