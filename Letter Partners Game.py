s, a = input(), list()
for i in s:
    if ord(i) - ord('a') >= 13 and (not a or ord(i) - ord(a.pop(-1)) != 13): print("Lost"); exit(0)
    if ord(i) - ord('a') < 13: a.append(i)
print("Won")
