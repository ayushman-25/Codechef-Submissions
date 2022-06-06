w, n, ans, wt = list(map(float, input().split())), int(input()), 0, 1
for i in w:
    if 0.2 <= i <= 0.7: pd = 0
    elif 0.71 <= i <= 1.2: pd = 1
    elif 1.21 <= i <= 1.7: pd = 2
    elif 1.71 <= i <= 2.2: pd = 3
    elif 2.21 <= i <= 2.7: pd = 4
    elif 2.71 <= i <= 3.2: pd = 5
    elif 3.21 <= i <= 3.7: pd = 6
    elif 3.71 <= i <= 4.2: pd = 7
    elif 4.21 <= i <= 4.7: pd = 8
    elif 4.71 <= i <= 5.2: pd = 9
    ans += pd * wt
    wt = 1 if wt == 3 else 3
print("Yes" if ans % 10 == n else "No")
