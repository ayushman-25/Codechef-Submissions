s, ans = input(), set()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        f1, f2 = 5 * int(s[i: j]) ** 2 + 4, 5 * int(s[i: j]) ** 2 - 4
        if f1 ** 0.5 == int(f1 ** 0.5) or f2 ** 0.5 == int(f2 ** 0.5):
            ans.add(int(s[i: j]))
print("None" if not ans else "\n".join(list(map(str, sorted(ans)))))
