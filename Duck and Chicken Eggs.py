from itertools import combinations
arr = [input().split() for _ in range(int(input()))]
for i in list(combinations(arr, 2)):
    c = [j for j in arr if j not in i]
    if (int(i[0][1]) + int(i[1][1])) << 1 == sum(int(j[1]) for j in c):
        print(i[0][0], i[1][0] + "\n" + " ".join([j[0] for j in c])); exit(0)
