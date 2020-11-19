import math

def findLargest(arr, n):  
    gcd = arr[0] 
    for i in range(1,n): 
        gcd = math.gcd(gcd, arr[i]) 
   
    return n if (gcd == 1) else -1


for _ in range(int(input())):
	n = int(input())
	arr = [int(i) for i in input().split()]
	ans = findLargest(arr, n)
	if ans == 1:
		print(-1)
	else:
		print(ans)