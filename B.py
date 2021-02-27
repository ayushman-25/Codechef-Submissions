s1, s2 = list(input()), list(input())
ans = ''
if(len(s1) > len(s2)):
    for i in range(0, len(s1) - len(s2)):
        ans += s1[i]
    s1 = s1[len(s1) - len(s2):]
elif(len(s2) > len(s1)):
    for i in range(0, len(s2) - len(s1)):
        ans += s2[i]
    s2 = s2[len(s2) - len(s1):]
for i in range(len(s1)):
    diff = ord(s1[i]) - ord(s2[i])
    if(diff == 0): ans += s1[i]
    elif(diff > 0): ans += chr(ord('a') + diff - 1)
    else: ans += chr(ord('a') + 26 - abs(diff))
print(ans)
