s1, s2 = input().split(), input().split()
if len(s1) != len(s2):
    print("Length different"); exit(0)
for i in range(len(s1)):
    if len(s1[i]) != len(s2[i]): print("Strings differ in space"); exit(0)
    if any(not j.isalpha() for j in s1[i]) or any(not j.isalpha() for j in s2[i]):
        print("Strings contain non alphabets"); exit(0)
print("Strings are", "not stepped" if any(len(s1[i]) * i + j + 1 != ord(s2[i][j]) - ord(s1[i][j])
            for i in range(len(s1)) for j in range(len(s1[i]))) else "stepped")
