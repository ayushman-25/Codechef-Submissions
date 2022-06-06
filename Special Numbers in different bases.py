n, b = input(), int(input())
print("Invalid" if any(int(i) > b - 1 for i in str(n)) else (
    "Yes" if int(str(n), b) == sum(int(i) ** len(n) for i in n) else "No"))
