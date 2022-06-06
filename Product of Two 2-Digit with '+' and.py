m = int(input())
n = int(input())
ans = 0
lt = list()
while 1:
    maxi = max(m, n)
    mini = min(m, n)
    m = mini
    n = maxi
    if m & 1:
        lt.append((m, n))
        ans += n
    if min(m, n) == 1:
        break
    m >>= 1
    n <<= 1
for i in lt[::-1]:
    print(*i)
print(ans)