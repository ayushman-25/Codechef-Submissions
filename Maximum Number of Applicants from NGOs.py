from collections import Counter
m, n = int(input()), int(input())
arr = list(map(int, input().split()))
ans = list(set(arr))
cnt = Counter(arr)
hmm = len(ans)
for i in sorted(set(ans)):
    can = cnt[i] - 2
    rem = max(0, can - ans.count(i))
    for j in range(rem):
        ans.append(i)
        hmm += 1
        if hmm == m:
            print(sum(ans) + m); exit(0)
if len(ans) != m:
    for j in range(m - len(ans)):
        ans.append(sorted(arr, reverse=True)[j])
print(sum(ans) + m)