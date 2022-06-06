n = int(input())
start, end, ans = 1, n, list()
while 1:
    ans.append([start, end])
    start += 1; end -= 1
    while n % start: start += 1
    while n % end: end -= 1
    if end <= start: break
print(len(ans))
print("\n".join([str(a) + ' ' + str(b) for [a, b] in ans]))