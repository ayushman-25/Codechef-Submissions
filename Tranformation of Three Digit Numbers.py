n, check, ans = input(), None, -1
if len(set(n)) == 1:
    print("No"); exit(0)
while check != '495':
    check = str(abs(int("".join(sorted(n)[::-1])) - int("".join(sorted(n)))))
    check = ('0' * (3 - len(check))) + check
    n = check
    ans += 1
print(ans)