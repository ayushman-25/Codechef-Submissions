from math import log2
a, x, y = int(input()), int(input()), int(input())
if (a ^ x == y): print("Correct transmission"); exit(0)
val = a ^ x
x = val // y if (val > y) else y // val
print("Shifted", "left" if (val > y) else "right", "by", int(log2(x)), "bits")