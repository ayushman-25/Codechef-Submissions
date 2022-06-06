queries, ways = [int(input()) for _ in range(int(input()))], [1, 2]
[ways.append((ways[-1] + ways[-2]) % (int(1e9) + 7)) for i in range(2, max(queries))]
print(*[ways[i - 1] for i in queries], sep='\n')
