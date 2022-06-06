print(*[' '.join(i) for i in [input().split() for _ in range(int(input()))] if i == sorted(i) or i == sorted(i)[::-1]], sep='\n')
