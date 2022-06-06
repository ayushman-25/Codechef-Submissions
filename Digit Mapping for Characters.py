s = input()
for i in range(10 ** len(s) - 1, -1, -1):
    if (i ** 0.5 == int(i ** 0.5) and len(set(str(i))) == len(str(i))):
        print(*[' '.join([s[j], str(i)[j]]) for j in range(len(s))], sep='\n')
        exit(0)
