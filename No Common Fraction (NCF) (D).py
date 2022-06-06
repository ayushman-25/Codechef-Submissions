u, l = int(input()), int(input())
print(len({a / b for a in range(l, u + 1) for b in range(max(2, l), u + 1) if 0.2 < a / b < 0.6}))