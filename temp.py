usual = input()
new=usual[:8]
check=usual[9:]
heaven = ""
if(check=='P.M' and new[:2] != '12'):
    new=str(int(new[:2])+12)+new[2:]
k = int(new[0:2])
if(usual == "12:00:00 midnight"):
    heaven = "08:00:00 midnight"
elif(new == "08:00:00"):
    heaven = "08:00:00 midmorning"
elif(new == "16:00:00"):
    heaven = "08:00:00 midevening"
elif(k<=7 and k>=0):
        heaven = usual[:8] + " A.M"
elif(k>=8 and k<=15):
    k = k-8
    b = "0" + str(k)
    heaven = b + usual[2:8] + " B.M"
elif(k>=16 and k<=23):
    k = k-16
    b = "0" + str(k)
    heaven = b + usual[2:8] + " C.M"


print(heaven)