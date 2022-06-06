# s = input()
# print("No" if any(int(s[0: i + 1]) % (len(s) - i) for i in range(len(s))) else "Yes")
n = int(input())
div = 1
while n:
    if n % div:
        print("No"); exit(0)
    n //= 10
    div += 1
print("Yes")