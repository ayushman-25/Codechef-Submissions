a, b, c = int(input()), int(input()), int(input())
arr = [a, b, c]
for i in range(int(input()) - 3):
    arr.append(arr[-1] + (c - b if (i & 1) else b - a))
print(arr[-1])