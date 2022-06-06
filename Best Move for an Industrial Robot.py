n, m, arr = int(input()), int(input()), list(map(int, input().split()))
ans = [arr[i: j] for i in range(m) for j in range(i + 1, m + 1)if sum(arr[i: j]) == n]
print("Not possible" if not ans else " ".join(list(map(str, sorted(ans, key=lambda x: len(x))[0]))))
