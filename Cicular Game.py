arr = [int(input()) for _ in range(int(input()))]
arr = [arr[-1]] + arr + [arr[0]]
fnd = False
for i in range(1, len(arr) - 1):
    if arr[i - 1] < arr[i] < arr[i + 1]:
        fnd = True
        print(i)
if not fnd:
    print("None")