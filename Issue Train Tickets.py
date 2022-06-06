a = [(int(input()), int(input())) for _ in range(4)]
print(*[i[0] for i in a if (i in sorted(a, key=lambda x: -x[1])[0:3])], sep='\n')
