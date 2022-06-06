n = int(input())
arr1 = [int(input()) for _ in range(n)]
m = int(input())
arr2 = [int(input()) for _ in range(m)]
L = list()
for i in range(min(n, m)):
    if arr1[i] % (i + 1) == 0: L.append(arr1[i])
    if arr2[i] % (i + 1) == 0: L.append(arr2[i])
for i in range(min(n, m), max(n, m)):
    if n > m and arr1[i] % (i + 1) == 0: L.append(arr1[i])
    if m > n and arr2[i] % (i + 1) == 0: L.append(arr2[i])
print(*[L[i] for i in range(len(L)) if (L[i] % (i + 1) == 0)], sep='\n')
