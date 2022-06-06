n, k = int(input()), int(input())
locker = list()
while n:
    locker.append(str(n % k))
    n //= k
print("".join(locker)[::-1])
print(sum(map(int, locker)))