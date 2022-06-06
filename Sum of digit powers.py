n = input()[::-1]
print(sum((i + 1) ** int(n[i]) for i in range(len(n))))