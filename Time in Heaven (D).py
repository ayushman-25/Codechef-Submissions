t = list(map(str, input().split(":")))
check = t[-1].split()[-1]
t[-1] = t[-1][0:2]
if check == "midnight": t[0] = t[1] = t[2] = '00'
if check == 'P.M' and t[0] != '12': t[0] = str(int(t[0]) + 12)
if t[0] == t[1] == t[2] == '00':
    print("08:00:00 midnight")
elif t[0] == '08' and t[1] == t[2] == '00':
    print("08:00:00 midmorning")
elif t[0] == '16' and t[1] == t[3] == '00':
    print("08:00:00 midevening")
elif 0 <= int(t[0]) <= 7:
    print(":".join(t), "A.M")
elif 8 <= int(t[0]) <= 15:
    t[0] = '0' + str(int(t[0]) - 8)
    print(":".join(t), 'B.M')
else:
    t[0] = '0' + str(int(t[0]) - 16)
    print(":".join(t), 'C.M')
