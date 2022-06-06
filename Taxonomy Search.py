from collections import defaultdict
txn = defaultdict(defaultdict)
for _ in range(int(input())):
    root, l1, d = input(), input().split(), defaultdict(str)
    for i in range(len(l1)):
        d[l1[i]] = input()
    txn[root] = d
p, l1, l2 = input(), input(), input()
print("Taxonomy", "present" if txn[p] and l2 in txn[p][l1] else "not present")