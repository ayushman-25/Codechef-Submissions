s1, s2 = input(), input()
cmn = [i for i in s1 if i in s2]
crsovr = lambda a, b, i: a[: a.index(i) + 1] + "".join([j for j in iter(lambda x=iter(b[b.index(i) + 1:]): next(x), i)])
print(*sorted([crsovr(s1, s2, i) for i in cmn] + [crsovr(s2, s1, i) for i in cmn]), sep='\n')