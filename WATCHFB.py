for _ in range(int(input())):
    n = int(input())
    cnt1, cnt2 = 0, 0
    fav, non_fav = 0, 0
    for i in range(n):
        a, b, c = map(int, input().split())
        if a == 1:
            fav = b
            non_fav = c
            print("YES")
        else:
            if b == c:
                print("YES")
                fav = b
                non_fav = c
                continue
            if (b < fav):
                print("YES")
                fav = c
                non_fav = b
                continue
            if (c < fav):
                print("YES")
                fav = b
                non_fav = c
                continue
            if (b < non_fav) and (non_fav > fav):
                print("YES")
                fav = b
                non_fav = c
                continue
            if (c < non_fav) and (non_fav > fav):
                print("YES")
                fav = c
                non_fav = b
            else:
                print("NO")