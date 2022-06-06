stock_price = list(map(int, input().split()))
q = int(input())
queries = list(map(int, input().split()))
[stock_price.append((stock_price[i-1] * 3 + stock_price[i-2] * 4) % (int(1e9) + 7)) for i in range(2, max(queries))]
print(*[stock_price[i - 1] for i in queries])