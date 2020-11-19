for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dishes = sorted(set(arr))
    max_till_now = 0
    best_dish = -1
    for i in dishes:
        temp = 0
        tempvar2 = 0
        for j in range(n):
            if arr[j] == i:
                temp += 1
            else:
                if temp == 1:
                    tempvar2 += 1
                else:
                    if temp % 2 == 0:
                        tempvar2 += (temp // 2)
                    else:
                        tempvar2 += ((temp // 2) + 1)
                temp = 0
            if j == n - 1:
                if temp > 0:
                    if temp == 1:
                        tempvar2 += 1
                    else:
                        if temp % 2 == 0:
                            tempvar2 += (temp // 2)
                        else:
                            tempvar2 += (temp // 2 + 1)
        if(max_till_now < tempvar2):
            max_till_now = tempvar2
            best_dish = i
    print(best_dish)


##########    OR      ###########

# from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dishes = sorted(set(arr))
    # ans_list = Counter()
    temp = arr[0]
    templ = []
    templl = []
    for i in range(n):
        if arr[i] == temp:
            templl.append(arr[i])
        else:
            templ.append(templl)
            templl = []
            templl.append(arr[i])
            temp = arr[i]
        if i == n - 1:
            if(len(templl) > 0):
                templ.append(templl)
    ans = 0
    temp = 0
    min_dish = -1
    # print(templ)
    # print(dishes)
    for i in dishes:
        for j in templ:
            if i == j[0]:
                if len(j) == 1:
                    temp += 1
                elif len(j) > 1:
                    if len(j) % 2 == 0:
                        temp += (len(j) // 2)
                    else:
                        temp += ((len(j) // 2) + 1)
        if ans < temp:
            ans = temp
            min_dish = i
        #ans_list[i] = temp
        temp = 0
    # print(ans_list)
    # print(ans_list.most_common(len(dishes))[0][0])
    print(min_dish)