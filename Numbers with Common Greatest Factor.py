n1, n2 = int(input()), int(input())
f1 = [i for i in range(2, n1) if n1 % i == 0]
f2 = [i for i in range(2, n2) if n2 % i == 0]
print("No" if not f1 or not f2 or f1[-1] != f2[-1] else f1[-1])
