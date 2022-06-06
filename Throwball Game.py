total = int(input())
arr = [input().split() for _ in range(int(input()))]
start, end, dec, temp = int(input()) - 1, input(), -1, None
throw = chr(ord('A') + start)
while temp != end:
    dec += 1
    fnd = [i for i in arr if i[0] == throw][0]
    throw = chr(ord('A') + int(fnd[1]) - 1)
    temp = fnd[0]
print(format((100 - (dec << 1)) / 100 * total, ".2f"))
