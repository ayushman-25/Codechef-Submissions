# cook your dish here
from collections import Counter

for _ in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    if n == len(set(arr)):
        print("YES")
        print(*sorted(arr))
        continue
    if arr.count(max(arr)) > 1:
        print("NO")
        continue
    hashi = Counter(arr).most_common(n)
    ans = True
    for i in hashi:
        if i[1] > 2:
            ans = False
            break
    if not ans:
        print("NO")
    else:
        ans = []
        sortedarr = sorted(set(arr))
        ans += sortedarr
        remans = []
        for i in hashi:
            if i[1] == 2:
                remans.append(i[0])
        remans.sort(reverse = True)
        ans += remans
        print("YES")
        print(*ans)