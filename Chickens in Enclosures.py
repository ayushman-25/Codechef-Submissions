n, m = int(input()), int(input())
ans = set((i, j, n - i - j) for i in range(m, n + 1) for j in range(i + 1, n + 1)
          if (i < n - i - j > j and i & 1 and j & 1 and (n - i - j) & 1))
print("No way" if not ans else "\n".join([" ".join(list(map(str, i))) for i in sorted(ans)]))
