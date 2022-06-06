s, i = list(input().lower()), 0
while i < len(s) - 1:
    if s[i] == s[i + 1]:
        j = i
        while j < len(s) and s[j] == s[i]: j += 1
        s[i: j] = '*'
        i = 0; continue
    if s[i] != '*' and s[i + 1] == '*':
        del s[i + 1]
        i = 0; continue
    i += 1
print(1 if s == ['*'] else 0)