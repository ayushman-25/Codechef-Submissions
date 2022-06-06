def add_extra(s1, s2):
    global f1, f2, f3, f4
    f1 += s2[len(s1):]
    f2 += s2[len(s1):]
    f3 += s2[::-1][len(s1):]
    f4 += s2[::-1][len(s1):]
    return max(f1, f2, f3, f4)


s1, s2 = input(), input()
f1 = ''.join(map(''.join, zip(s1, s2)))
f2 = ''.join(map(''.join, zip(s2, s1)))
f3 = ''.join(map(''.join, zip(s1[::-1], s2[::-1])))
f4 = ''.join(map(''.join, zip(s2[::-1], s1[::-1])))

print(add_extra(s1, s2) if len(s1) < len(s2) else add_extra(s2, s1))