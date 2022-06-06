a = [int(input()) for _ in range(int(input()))]
a = [a[-1]] + a + [a[0]]
ans = [str(i) + "\n" for i in range(1, len(a) - 1) if (a[i - 1] < a[i] < a[i + 1])]
print("None" if not ans else "".join(ans))