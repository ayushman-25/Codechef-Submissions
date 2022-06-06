for _ in range(int(input())):
    n = int(input())
    status = list(input())
    ans = 0
    if status == ['0']:
        print(1)
        continue
    for i in range(n):
        if status[i] == '0':
            if i == 0:
                if status[i + 1] != '1':
                    status[i] = '1'
                    ans += 1
            elif i == n - 1:
                if status[i - 1] != '1':
                    status[i] = '1'
                    ans += 1
            else:
                if (status[i - 1] == status[i + 1] == '0'):
                    status[i] = '1'
                    ans += 1
    #print(status)
    print(ans)