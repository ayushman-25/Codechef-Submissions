def f(x):
    if x <= 6:
        return 15
    if x <= 8:
        return 20
    if x <= 10:
        return 25
    if x > 61:
        return f(x - (10 * ((x-50)//10))) + ((x-50)//10)*25
    return min(15 + f(x-6), 20 + f(x-8), 25 + f(x-10))
 
 
for _ in range(int(input())):
    n = int(input())
    print(f(n))