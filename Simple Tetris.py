q, stack = int(input()), list()
for _ in range(q):
    arr = list(map(str, input().split()))
    if arr[0] == '1':
        stack.append(arr[-1])
        if len(stack) >= 4 and len(set(stack[-4:])) == 1:
            del stack[-4:]
        continue
    print(len(stack))