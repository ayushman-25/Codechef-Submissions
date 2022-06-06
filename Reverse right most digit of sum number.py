a, b = input(), input()
print("".join(['9' if (i == 2 and not((int(a[i]) + int(b[i])) % 10)) else str((int(a[i]) + int(b[i])) % 10) for i in range(2, -1, -1)]))