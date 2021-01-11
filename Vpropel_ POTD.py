from math import factorial
n = int(input())
for i in range(1, n):
    if(factorial(i) == n): break
    if(factorial(i) > n): print(-1); exit(0)
prod = 1
if(i & 1):
    for j in range(1, i + 1, 2): prod *= j
else:
    for j in range(2, i + 1, 2): prod *= j
print(prod)
