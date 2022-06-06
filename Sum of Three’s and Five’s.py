n = int(input())
if (n % 3 == 0):
    print("Only three's"); exit(0)
if (n % 5 == 0):
    print("Only five's"); exit(0)
ans = set()
for three in range(1, 1000):
    for five in range(1, 1000):
        if (three * 3 + five * 5 == n):
            ans.add((three, five))
if not ans:
    print("Invalid input"); exit(0)
fin = list(sorted(ans)[-1])
print(fin[0], "three's and", fin[1], "five's")