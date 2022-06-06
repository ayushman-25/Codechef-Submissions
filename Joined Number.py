s, sm = input(), int(input())
print(*[s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if sum(int(k) for k in s[i: j]) == sm]
      , sep='\t')
