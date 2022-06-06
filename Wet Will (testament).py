from math import ceil
sm = sum(int(i) for i in input())
check = 9 * ceil(sm / 9)
print(check - sm if check - sm else 9)