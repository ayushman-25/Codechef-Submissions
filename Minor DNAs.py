from itertools import combinations
print(*sorted(["".join(i) for i in combinations(input(), int(input()))]), sep='\n')