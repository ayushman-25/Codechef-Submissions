from collections import defaultdict
d, b, s, a = [input().lower() for _ in range(int(input()))], defaultdict(int), -1, 0
for i in d: b[i] = sum(j < min(i[0], i[-1]) or j > max(i[0], i[-1]) for j in i[1:-1])
for i in range(len(d)):
    a += abs(s - b[d[i]])
    if(not(s - b[d[i]])): print('n', end='\t')
    else: [print('f', end='\t') if(b[d[i]] > s) else print('b', end='\t')]
    print(abs(s - b[d[i]]))
    s = b[d[i]]
print(a)