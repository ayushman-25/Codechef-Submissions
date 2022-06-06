s1, s2, f = input().lower(), input().lower(), lambda s: 'a' if (s == 'z') else chr(ord(s) + 1)
for _ in range(2, int(input())):
    s1, s2 = s2, "".join([f(s2[i] if (i & 1) else s1[i]) for i in range(len(s1))])
print(s2)
