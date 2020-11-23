alp = [chr(i) for i in range(97, 123)]
s1, s2 = input(), input()
n = int(input())
l1, l2 = s1, s2
for _ in range(n - 2):
    ns1 = ''
    for i in range(len(l1)):
        if(i % 2 == 0):
            ns1 += alp[(ord(l1[i]) - ord('a') + 1) % 26]
        else:
            ns1 += alp[(ord(l2[i]) - ord('a') + 1) % 26]
    l1 = l2
    l2 = ns1
print(ns1)