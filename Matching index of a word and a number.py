d, n, s = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)], input(), input()
if len(s) << 1 != len(n):
    print(-1); exit(0)
print(sum("".join([d[int(n[i] + n[i + 1]) % 52 - 1] for i in range(0, len(n), 2)])[i] == s[i] for i in range(len(s))))
