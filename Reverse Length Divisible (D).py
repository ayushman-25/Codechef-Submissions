n = int(input())
for i in range(1, len(str(n))):
    if (int(str(n)[0: i]) % (len(str(n)) - i + 1)):
        print("No"); exit(0)
print("Yes")
