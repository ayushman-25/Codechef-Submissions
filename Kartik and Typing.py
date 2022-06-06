time, already = 0, dict()
find_time = lambda i: 2 + sum(
    (4 if i[k] in 'df' else 2) if i[k - 1] in 'df' else (2 if i[k] in 'df' else 4) for k in range(1, len(i)))
for i in [input() for _ in range(int(input()))]:
    time += already[i] >> 1 if i in already else find_time(i)
    already[i] = find_time(i)
print(time)
