s, roman = input(), {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
arr, curr_cnt, bffr, ans = list(), 1, roman[s[0]], 0
if('VV' in s or 'LL' in s or 'DD' in s): print("Invalid"); exit(0)
for i in range(len(s) - 1):
    if(roman[s[i]] == roman[s[i + 1]]): curr_cnt += 1
    else:
        if(roman[s[i + 1]] > roman[s[i]] and  curr_cnt > 2): print("Invalid"); exit(0)
        else: curr_cnt = 1
for i in range(1, len(s)):
    if(roman[s[i]] == roman[s[i - 1]]): bffr += roman[s[i]]
    else: arr.append(bffr); bffr = roman[s[i]]
if(bffr): arr.append(bffr)
print(sum(arr[i] if (arr[i] >= arr[i + 1]) else -arr[i] for i in range(len(arr) - 1)) + arr[-1])