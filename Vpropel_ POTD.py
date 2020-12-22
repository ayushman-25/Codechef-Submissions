alp = 'abcdefghijklmnopqrstuvwxyz '
s1, s2 = input(), input()
if(len(s1) != len(s2)):
    print("Length different"); exit(0)
for i in range(len(s1)):
    if(s1[i] not in alp) or (s2[i] not in alp):
        print("Strings contain non alphabets"); exit(0)
for i in range(len(s1)):
    if(s1[i] == ' ' and s2[i] != ' ') or (s2[i] == ' ' and s1[i] != ' '):
        print("Strings differ in space"); exit(0)
s1 = s1.replace(' ', ''); s2 = s2.replace(' ', '')
for i in range(len(s1)):
    check = abs(alp.index(s1[i]) - alp.index(s2[i]))
    if(check != i + 1 and 26 - check != i + 1):
            print("Strings are not stepped"); exit(0)
print("Strings are stepped")