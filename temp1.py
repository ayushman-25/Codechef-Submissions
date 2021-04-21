from math import sqrt

def isPrime(n):
    if (n <= 1): return False
    if (n <= 3): return True
    if (n % 2 == 0 or n % 3 == 0): return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0): return False
        i = i + 6
    return True


def fPF(n):
    s = set()
    while (n % 2 == 0):
        s.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0):
            s.add(i)
            n = n // i
    if (n > 2):
        s.add(n)
    return s


def fP(n):
    if (isPrime(n) == False): return -1
    phi = n - 1
    p = fPF(phi)
    for r in range(2, phi + 1):
        flag = False
        for it in p:
            if (pow(r, phi // it, n) == 1):
                flag = True
                break
        if (flag == False):
            return r
    return -1


def euler_totient(n):
    result = n
    p = 2
    while (p * p <= n):
        if (n % p == 0):
            while (n % p == 0): n = int(n / p)
            result -= int(result / p)
        p += 1
    if (n > 1): result -= int(result / n)
    return result


n = int(input())
print(fP(n), euler_totient(n - 1))