n = int(input())
l = r = ((n << 1) - 1) >> 1
for _ in range(n):
    print(*['.' if l != i != r else '*' for i in range((n << 1) - 1)])
    l -= 1; r += 1
