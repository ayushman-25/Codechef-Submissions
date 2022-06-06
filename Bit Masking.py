x = int(input()) ^ int(input())
print(*[i + 1 for i in range(32) if not((x >> i) & 1)])
