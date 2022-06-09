arr = list()
while 1:
    x = int(input())
    if x == -1:
        break
    arr.append(x)
arr.insert(int(input()) - 1, int(input()))
print(*[i for i in arr], sep='\t', end='\t')
print()
print(*[format(sum(arr[i: i + 3]) / 3, '.2f') for i in range(0, len(arr) - 2)], sep='\t'
