x, p, q = int(input()), int(input()), int(input())
week, curr = 1, 0
while (1):
    curr += p
    p += q
    if (curr >= x):
        print(week); break
    week += 1

