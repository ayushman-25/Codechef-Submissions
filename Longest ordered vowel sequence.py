s = input().split()
vowel = "aeiou"
ans = list()
for i in s:
    l = 0
    vow = list()
    for j in range(len(i)):
        if i[j] in vowel and i[j] not in vow:
            vow.append(i[j])
    if len(vow) > 1:
        for j in range(1, len(vow)):
            if vow[j] <= vow[j - 1]:
                del vow[j:]
                break
    ans.append((i, len(vow)))
ans.sort(key=lambda x: [-x[1]])
for i in ans:
    if i[1] == ans[0][1]:
        print(i[0])