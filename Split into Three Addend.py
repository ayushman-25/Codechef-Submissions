n, a, b = int(input()), int(input()), int(input())
a1 = [max(a, b), min(a, b), min(a, b)]
a2 = [max(a, b), max(a, b), min(a, b)]
if (sum(a1) == n):
    print(*a1)
elif (sum(a2) == n):
    print(*a2)
else:
    print("Cannot be written")