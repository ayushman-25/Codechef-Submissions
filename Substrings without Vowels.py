s, n = input(), int(input())
print(*[s[i: i + n] for i in range(len(s) - n + 1) if all(j not in 'aeiou' for j in s[i: i + n])], sep='\n')
