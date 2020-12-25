from collections import Counter
print(0 if Counter(input().lower()).most_common(1)[0][1] == 1 else 1)
