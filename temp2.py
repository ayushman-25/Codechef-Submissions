from collections import defaultdict
txnmy = defaultdict(list)
for _ in range(int(input())):
    strr = input()
    lvl1 = list(map(str, input().split()))
    txnmy[strr] = [[lvl1[i], list(map(str, input().split()))] for i in range(len(lvl1))]
p, l1, l2 = input(), input(), input()
print("Taxonomy present" if(txnmy[p] and txnmy[p][0][0] == l1 and l2 in txnmy[p][0][1: ][0]) else "Taxonomy not present")