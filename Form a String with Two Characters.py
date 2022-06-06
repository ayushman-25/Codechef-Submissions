from itertools import combinations
s, a = input(), list()
for i in filter(lambda x: x[0] != x[1], combinations(s, 2)):
    t = s.replace(i[0], '')
    t = t.replace(i[1], '')
    if all(t[k - 1] == t[k] or t[k] == t[k + 1] for k in range(1, len(t) - 1)):
        a.append(t)
print(sorted(a, key=lambda x: [-len(x), x])[0])