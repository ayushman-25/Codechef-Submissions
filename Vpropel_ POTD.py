s, n, cnt = input(), int(input()), 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        cnt += (sum((k in 'aeiou') for k in s[i: j]) == n)
print(cnt)