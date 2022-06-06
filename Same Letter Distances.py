from collections import Counter

s = input()
ans = [i for i in range(len(s)) if (s[i] == Counter(s).most_common(len(s))[0][0])]
print(Counter(s).most_common(len(s))[0][0])
for i in range(1, len(ans)):
    check = ans[i] - ans[i - 1] - 1
    print(check if check else "No", "character" if (check == 1) else "characters")