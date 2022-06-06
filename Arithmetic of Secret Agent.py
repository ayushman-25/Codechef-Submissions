alp = 'abcdefghijklmnopqrstuvwxyz'
ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s1, s2 = input()[::-1], input()[::-1]
ans = ""
carry = 0
for i in range(min(len(s1), len(s2))):
    hmm = ord(s1[i]) + ord(s2[i]) + carry
    if hmm <= 9:
        carry = 0
    else:
        carry = int(str(hmm)[:-1])

    ans += str(hmm)[-1]
print(ans)