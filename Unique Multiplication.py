a, b = input(), input()
prod = str(int(a) * int(b))
if ("".join(sorted(set(a + b + prod))) == '123456789'):
    for i in a:
        if i in b:
            print("No"); exit(0)
    for i in a:
        if i in prod:
            print("No"); exit(0)
    for i in b:
        if i in prod:
            print("No"); exit(0)
    print("Yes")
    exit(0)
print("No")