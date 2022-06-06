arr = [input()[::-1] for _ in range(int(input()))]
for i in range(1, len(arr)):
    if sorted([arr[i], arr[i - 1]]) != [arr[i - 1], arr[i]]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
print(*[i[::-1] for i in arr], sep='\n')