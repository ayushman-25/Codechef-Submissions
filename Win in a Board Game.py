n = int(input())
x, y = map(int, input().split())
for _ in range(int(input())):
    s = input()
    x, y = x + (x < n - 1 and s == 'u') - (x > 0 and s == 'd'), y + (y < n - 1 and s == 'r') - (y > 0 and s == 'l')
f1, f2 = map(int, input().split())
print("Win" if (f1 == x and f2 == y) else "Loss")
