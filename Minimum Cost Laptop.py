budget = int(input())
info = [list(map(int, input().split())) for _ in range(int(input()))]
info.sort(key=lambda x: [-x[0] * x[1]])
for i in info:
    if i[-1] <= budget:
        print(*i); exit(0)
print("No laptop")