from math import ceil, floor
n = int(input())
x1, y1 = n >> 1, (n >> 1) + 1 if n & 1 else n >> 1
prod = x1 * y1 - (12 if n & 1 else 9)
check = n / 5
x, y = ceil(check * 2), ceil(check * 3)
if x * y == prod and x + y == n:
    print(x, y, sep='\n')
x, y = ceil(check * 2), floor(check * 3)
if x * y == prod and x + y == n:
    print(x, y, sep='\n')
x, y = floor(check * 2), ceil(check * 3)
if x * y == prod and x + y == n:
    print(x, y, sep='\n')
x, y = floor(check * 2), floor(check * 3)
if x * y == prod and x + y == n:
    print(x, y, sep='\n')