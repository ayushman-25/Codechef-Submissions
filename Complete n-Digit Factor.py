n, m, fnd = int(input()), int(input()), False
for i in range(2, 10 ** m + 1):
    if (10 ** n + 1) % i == 0:
        print(i); fnd = True
if not fnd:
    print("No complete factors")