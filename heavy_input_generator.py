from random import *
print(15)
for _ in range(15):
    choosee = ['?', 'C', 'H', 'E', 'F']
    ans = ''
    for i in range(10):
        ans += choice(choosee)
    print(ans)