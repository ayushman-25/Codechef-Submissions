a, b, j = input(), input(), 0
for i in range(len(a)):
    if a[i] == b[j]: j += 1
    if j == len(b): print("Yes"); exit(0)
print("No")
