lt = [int(input()) for _ in range(int(input()))]
m = int(input())
answer = list()
start = 0
for i in lt:
    start += 1
    check = bin(m ^ i).count('1')
    answer.append((check, start, i))
answer.sort()
for i in answer:
    if i[0] == answer[0][0]:
        print(i[2])