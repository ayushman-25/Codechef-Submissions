w1, w2 = input(), input()
for i in range(len(w1)):
    if (w1[i] in 'aeiou' and w1[i] and w2):
        print(w1[:i] + w2[w2.index(w1[i]):])
        exit(0)