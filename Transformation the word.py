s = input()
f, p = [int(input()) for _ in range(len(s))], list()
for i in range(len(s)):
    p.insert(f[i] - 1, s[i])
print("".join(p), *[{s[i]: i + 1 for i in range(len(s))}[i] for i in p], sep='\n')
