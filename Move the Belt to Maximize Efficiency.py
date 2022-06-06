n, b = input(), input()
print(sorted(
    [(len(n[i: j]), i + 1, len(b) - b[::-1].index(n[i: j])) for i in range(len(n)) for j in range(i + 1, len(n) + 1) if
     n[i: j] in b[::-1]], key=lambda x: [-x[0], x[1]])[0], sep='\n')
