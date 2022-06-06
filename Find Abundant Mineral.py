from collections import Counter
print(Counter("".join([input() for _ in range(int(input()))])).most_common(1)[0][0])
