n = input()
if (not int(n[-2] + n[-1])):
    print("Division cannot be performed"); exit(0)
print(int(n) % int(n[-2] + n[-1]))
