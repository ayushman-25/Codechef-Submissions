def findCnt(arr, n, k) : 
    ret = 0;   
    i = 0;  
    while (i < n) :  
        j = i + 1;   
        while (j < n and arr[j] >= arr[j - 1]) : 
            j += 1;  
        x = max(0, j - i - k);  
        ret += (x * (x + 1)) / 2;  
        i = j; 
    return int(ret)

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	print(findCnt(arr, n, 1) + n)