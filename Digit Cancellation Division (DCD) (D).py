from collections import Counter as C
x, y = input(), input()
nx = "".join(list((C(x) - C(y)).elements()))
ny = "".join(list((C(y) - C(x)).elements()))
check = lambda s: s if s else '1'
print("-1.00" if not int(check(ny)) else "%0.2f" % (int(check(nx)) / int(check(ny))))
