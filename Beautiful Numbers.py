from itertools import product
n = int(input())
for i in [j for i in range(1, 14) for j in list(product([8, 9], repeat=i))]:
    if not(n % int("".join(list(map(str, i))))):
        print("beautiful"); exit(0)
print(-1)