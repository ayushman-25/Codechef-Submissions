import math
for x in range(int(input())):
    y, s = input(), 0
    if(len(y) > 2):
        for i in y:
            s += ord(i)
        print(chr(math.floor(s / len(y))))