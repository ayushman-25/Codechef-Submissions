n, it = int(input()), 0
while (1):
    it += 1
    n = sum(int(str(n)[i]) ** 2 for i in range(len(str(n))))
    if (it > 10):
        print("No"); exit(0)
    if (n == 4):
        print(it); exit(0)

