n = input()
print("No" if int(n[:2]) % int(n[2:]) else "Yes")