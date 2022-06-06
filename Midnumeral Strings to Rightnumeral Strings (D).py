stack, ans = list(), list()
for i in input():
    if i.isalpha(): ans.append(i)
    elif i == '(': stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            ans.append(stack.pop())
        stack.pop()
    else:
        while stack and i <= stack[-1]:
            ans.append(stack.pop())
        stack.append(i)
print("".join(ans + stack[::-1]))