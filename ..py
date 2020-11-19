arr = [2, 5, 6, 7, 3, 4, 6, 4, 3, 4, 6, 45, 6, 4, 534, 34, 3,5 6, 6, 464, 66,4 6]

k = 7

tempsum = 0
for i in arr:
    tempsum += (arr & k)

print(tempsum)

print(sum(arr) & k)